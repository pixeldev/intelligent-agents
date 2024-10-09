import flet

from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class MainScreenViewUi(ViewUi):
  def __init__(self, view_service: ViewUiService):
    super().__init__(ViewUiConstants.MAIN_SCREEN_IDENTIFIER)
    self.__view_service: ViewUiService = view_service

  def create_control(self) -> list[flet.Control]:
    return [flet.Column(
      [
        flet.Text("Menú Principal", style=UiConstants.TITLE_TEXT_STYLE),
        flet.ElevatedButton(
          "Jugar",
          on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAIN_SCREEN_IDENTIFIER),
          style=UiConstants.BUTTON_STYLE,
          width=500),
        flet.ElevatedButton(
          "Crear",
          on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.CREATION_MAIN_SCREEN_IDENTIFIER),
          style=UiConstants.BUTTON_STYLE,
          width=500),
        flet.ElevatedButton(
          "Editar",
          on_click=lambda _: self.__view_service.navigate_to(ViewUiConstants.EDITION_MAIN_SCREEN_IDENTIFIER),
          style=UiConstants.BUTTON_STYLE,
          width=500),
        flet.ElevatedButton(
          "Salir",
          on_click=lambda _: self.__view_service.close(),
          style=UiConstants.BUTTON_STYLE,
          width=500),
      ],
      alignment=flet.MainAxisAlignment.CENTER,
      horizontal_alignment=flet.CrossAxisAlignment.CENTER
    )]
