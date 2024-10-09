from typing import Optional

import flet
import flet as ft

from src.agent.domain.agent import Agent
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.environment import Environment
from ui.view.view_ui import ViewUi
from ui.ui_constants import UiConstants
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class PlayAgentSelectionViewUi(ViewUi):
  def __init__(self, environment_service: EnvironmentService, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_AGENT_SELECTION_SCREEN_IDENTIFIER)
    self.__environment_service: EnvironmentService = environment_service
    self.__view_service: ViewUiService = view_service

  def on_click(self, selected_agent: Agent) -> None:
    print(f'Seleccionado: {selected_agent}')
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is not None:
      environment.set_selected_agent(selected_agent)
    self.__view_service.navigate_to(ViewUiConstants.PLAY_AGENT_POSITION_SELECTION_SCREEN_IDENTIFIER)

  def create_control(self) -> list[flet.Control]:
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is None:
      return [
        ft.Column(
          [
            ft.Text("No se ha seleccionado un mapa", style=UiConstants.TITLE_TEXT_STYLE),
            ft.ElevatedButton(
              "Volver a la selección de mapa",
              on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER),
              style=UiConstants.BUTTON_STYLE)
          ],
          alignment=ft.MainAxisAlignment.CENTER,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
      ]

    agent_cards: list[ft.Control] = [
      ft.Card(
        content=ft.Column(
          [
            ft.Text(agent.get_name(), style=UiConstants.NORMAL_TEXT_STYLE),
            ft.ElevatedButton(
              "Seleccionar",
              on_click=lambda e, selected_agent=agent: self.on_click(selected_agent),
              style=UiConstants.BUTTON_STYLE
            )
          ],
          alignment=ft.MainAxisAlignment.CENTER,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=350,
        height=350,
      ) for agent in environment.get_agents()
    ]

    if len(agent_cards) == 0:
      return [
        ft.Column(
          [
            ft.Text("No se han definido agentes", style=UiConstants.TITLE_TEXT_STYLE),
            ft.ElevatedButton(
              "Volver a la selección de mapa",
              on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER),
              style=UiConstants.BUTTON_STYLE)
          ],
          alignment=ft.MainAxisAlignment.CENTER,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
      ]

    return [
      ft.Column(
        [
          ft.Text("Seleccionar Agente", style=UiConstants.TITLE_TEXT_STYLE),
          ft.Row(agent_cards, alignment=ft.MainAxisAlignment.CENTER),
          ft.ElevatedButton(
            "Volver a la selección de mapa",
            on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER),
            style=UiConstants.BUTTON_STYLE)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      )
    ]
