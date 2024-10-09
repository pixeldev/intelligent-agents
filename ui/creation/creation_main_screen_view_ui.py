import flet

from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class CreationMainScreenViewUi(ViewUi):
  def __init__(self, view_service: ViewUiService):
    super().__init__(ViewUiConstants.CREATION_MAIN_SCREEN_IDENTIFIER)
    self.__view_service = view_service

  def create_control(self) -> list[flet.Control]:
    return self.__view_service.create_control(ViewUiConstants.CREATION_TERRAIN_SELECTION_SCREEN_IDENTIFIER)
