from typing import Optional

import flet
from click import style
from rich.cells import cell_len

from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor import SensorResult
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.environment.application.environment_agent_service import EnvironmentAgentService, ExecuteSensorResult
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


# noinspection DuplicatedCode
class PlayGameSensorsViewUi(ViewUi):
  def __init__(self, environment_agent_service: EnvironmentAgentService, environment_service: EnvironmentService, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_GAME_SENSORS_SCREEN_IDENTIFIER)
    self.__environment_agent_service: EnvironmentAgentService = environment_agent_service
    self.__environment_service: EnvironmentService = environment_service
    self.__view_service: ViewUiService = view_service

  def create_control(self) -> list[flet.Control]:
    if self.__environment_service.get_environment() is None:
      return [
        flet.Text('No se ha seleccionado un mapa', style=UiConstants.TITLE_TEXT_STYLE),
        flet.ElevatedButton('Regresar', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER))
      ]

    environment: Environment = self.__environment_service.get_environment()
    selected_agent: Optional[Agent] = environment.get_selected_agent()

    if selected_agent is None:
      return [
        flet.Text('No se ha seleccionado un agente', style=UiConstants.TITLE_TEXT_STYLE),
        flet.ElevatedButton('Regresar', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.__view_service.navigate_to(ViewUiConstants.PLAY_AGENT_SELECTION_SCREEN_IDENTIFIER))
      ]

    sensors: list[SensorConfiguration] = selected_agent.list_sensors()
    sensors_controls: list[flet.Control] = []
    for sensor in sensors:
      sensors_controls.append(flet.Card(
        content=flet.Column(
          [
            flet.Text(sensor.get_name(), style=UiConstants.NORMAL_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
            flet.Text(sensor.get_description(), style=UiConstants.MEDIUM_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
            flet.Text(f'Radio: {sensor.get_radius()}', style=UiConstants.MEDIUM_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
            flet.Text(f'Puede atravesar obstáculos: {"Sí" if sensor.can_pass_trough() else "No"}', style=UiConstants.MEDIUM_TEXT_STYLE),
            flet.ElevatedButton(
              "Usar",
              on_click=lambda e, selected_sensor=sensor: self.on_use_click(selected_sensor),
              style=UiConstants.BUTTON_STYLE
            )
          ],
          alignment=flet.MainAxisAlignment.CENTER,
          horizontal_alignment=flet.CrossAxisAlignment.CENTER
        ),
        width=350,
        height=350
      ))

    return [
      flet.Column(
        controls=[
          flet.Text('Sensores', style=UiConstants.TITLE_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
          flet.Container(
            content=flet.ListView(
              controls=sensors_controls,
              horizontal=True
            ),
            width=1200,
            height=400,
            padding=25
          ),
          flet.ElevatedButton('Regresar', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_SCREEN_IDENTIFIER))
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER
      )
    ]

  def on_use_click(self, selected_sensor: SensorConfiguration) -> None:
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is None:
      return
    selected_agent: Optional[Agent] = environment.get_selected_agent()
    if selected_agent is None:
      return
    execute_sensor_result: ExecuteSensorResult = self.__environment_agent_service.execute_sensor(selected_agent, environment, selected_sensor)
    sensor_result: SensorResult = execute_sensor_result.get_sensor_result()
    if sensor_result is SensorResult.SUCCESS:
      self.__view_service.show_alert('Sensor ejecutado correctamente')
    elif sensor_result is SensorResult.UNKNOWN_CELL:
      self.__view_service.show_alert('No se puede detectar en esa dirección')
    elif sensor_result is SensorResult.OUT_OF_BOUNDS:
      self.__view_service.show_alert('Fuera de los límites del mapa')
    elif sensor_result is SensorResult.HIT_OBSTACLE:
      self.__view_service.show_alert('Se ha encontrado un obstáculo')
    else:
      self.__view_service.show_alert('Error al ejecutar el sensor')
    self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_SCREEN_IDENTIFIER)
