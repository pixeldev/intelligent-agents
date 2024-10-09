from src.environment.domain.terrain.terrain_repository import TerrainRepository
from ui.element_selection_view_ui import ElementSelectionViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class CreationTerrainSelectionViewUi(ElementSelectionViewUi):
  def __init__(self, terrain_repository: TerrainRepository, view_service: ViewUiService):
    super().__init__(ViewUiConstants.CREATION_TERRAIN_SELECTION_SCREEN_IDENTIFIER, view_service)
    self.__terrain_repository = terrain_repository

  def get_title(self) -> str:
    return 'Seleccionar Mapeo de Terreno'

  def get_elements(self) -> list[str]:
    return self.__terrain_repository.get_all_from_directory()

  def on_click(self, selected_element_name: str) -> None:
    print('Selected terrain:', selected_element_name)

  def get_previous_view_identifier(self) -> str:
    return ViewUiConstants.MAIN_SCREEN_IDENTIFIER
