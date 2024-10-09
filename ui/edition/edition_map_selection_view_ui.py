from src.map.domain.map_repository import MapRepository
from ui.element_selection_view_ui import ElementSelectionViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class EditionMapSelectionViewUi(ElementSelectionViewUi):
  def __init__(self, map_repository: MapRepository, view_service: ViewUiService):
    super().__init__(ViewUiConstants.EDITION_MAP_SELECTION_SCREEN_IDENTIFIER, view_service)
    self.__map_repository = map_repository

  def get_title(self) -> str:
    return 'Seleccionar Mapa para Editar'

  def get_elements(self) -> list[str]:
    return self.__map_repository.list_all_from_directory()

  def on_click(self, selected_element_name: str) -> None:
    print(f'Se ha seleccionado el mapa {selected_element_name}')

  def get_previous_view_identifier(self) -> str:
    return ViewUiConstants.MAIN_SCREEN_IDENTIFIER
