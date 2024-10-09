from typing import Optional

import flet
from click import style
from rich.cells import cell_len

from src.agent.domain.action.action import ActionResult
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.environment.application.environment_agent_service import EnvironmentAgentService, ExecuteActionResult
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


# noinspection DuplicatedCode
class PlayGameActionsViewUi(ViewUi):
  def __init__(self, environment_agent_service: EnvironmentAgentService, environment_service: EnvironmentService, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_GAME_ACTIONS_SCREEN_IDENTIFIER)
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

    actions: list[ActionConfiguration] = selected_agent.list_actions()
    action_controls: list[flet.Control] = []
    for action in actions:
      action_controls.append(flet.Card(
        content=flet.Column(
          [
            flet.Text(action.get_name(), style=UiConstants.NORMAL_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
            flet.Text(action.get_description(), style=UiConstants.MEDIUM_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
            flet.ElevatedButton(
              "Usar",
              on_click=lambda e, selected_action=action: self.on_use_click(selected_action),
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
          flet.Text('Acciones', style=UiConstants.TITLE_TEXT_STYLE, text_align=flet.TextAlign.CENTER),
          flet.Container(
            content=flet.ListView(
              controls=action_controls,
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

  def on_use_click(self, selected_action: ActionConfiguration) -> None:
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is None:
      return
    selected_agent: Optional[Agent] = environment.get_selected_agent()
    if selected_agent is None:
      return
    execute_action_result: ExecuteActionResult = self.__environment_agent_service.execute_action(selected_agent, environment, selected_action)
    action_result: ActionResult = execute_action_result.get_action_result()
    if execute_action_result.get_action_result() == ActionResult.GOAL_REACHED:
      self.__view_service.show_alert('¡Has llegado a la meta!')
    elif action_result == ActionResult.SUCCESS:
      self.__view_service.show_alert('Acción realizada con éxito')
    elif action_result == ActionResult.INVALID_PROPERTY:
      self.__view_service.show_alert('Propiedad inválida')
    elif action_result == ActionResult.OUT_OF_BOUNDS:
      self.__view_service.show_alert('Fuera de los límites')
    elif action_result == ActionResult.HIT_OBSTACLE:
      self.__view_service.show_alert('Chocaste con un obstáculo')
    elif action_result == ActionResult.UNKNOWN_CELL:
      self.__view_service.show_alert('Celda desconocida')
    elif action_result == ActionResult.UNKNOWN_DIRECTION:
      self.__view_service.show_alert('Dirección desconocida')
    else:
      self.__view_service.show_alert('Error al realizar la acción')
    self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_SCREEN_IDENTIFIER)
