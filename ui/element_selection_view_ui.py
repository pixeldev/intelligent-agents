from abc import abstractmethod, ABC

import flet

from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_repository import ViewUiService


class ElementSelectionViewUi(ViewUi, ABC):
  def __init__(self, identifier: str, view_service: ViewUiService):
    super().__init__(identifier)
    self._view_service = view_service

  @abstractmethod
  def get_title(self) -> str:
    pass

  @abstractmethod
  def get_elements(self) -> list[str]:
    pass

  @abstractmethod
  def on_click(self, selected_element_name: str) -> None:
    pass

  @abstractmethod
  def get_previous_view_identifier(self) -> str:
    pass

  def create_control(self) -> list[flet.Control]:
    buttons: list[flet.Control] = [flet.ElevatedButton(
      element_name,
      style=UiConstants.BUTTON_STYLE,
      width=1000,
      on_click=lambda e, selected_element_name=element_name: self.on_click(selected_element_name)) for element_name in
      self.get_elements()]

    return [flet.Column(
        [
          flet.Text(self.get_title(), style=UiConstants.TITLE_TEXT_STYLE),
          flet.Container(
            flet.Column(buttons, scroll=flet.ScrollMode.AUTO, alignment=flet.MainAxisAlignment.CENTER),
            width=1024,
            height=512,
            border=flet.border.all(width=2, color="black"),
            padding=25
          ),
          flet.ElevatedButton(
            "Volver",
            on_click=lambda _: self._view_service.navigate_to(self.get_previous_view_identifier()),
            style=UiConstants.BUTTON_STYLE)
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
      )]
