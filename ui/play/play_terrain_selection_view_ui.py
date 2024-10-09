from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from ui.element_selection_view_ui import ElementSelectionViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class PlayTerrainSelectionViewUi(ElementSelectionViewUi):
  def __init__(self, environment_service: EnvironmentService, terrain_repository: TerrainRepository, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_TERRAIN_SELECTION_SCREEN_IDENTIFIER, view_service)
    self.__environment_service = environment_service
    self.__terrain_repository = terrain_repository

  def get_title(self) -> str:
    return 'Seleccionar Mapeo de Terreno'

  def get_elements(self) -> list[str]:
    return self.__terrain_repository.get_all_from_directory()

  def on_click(self, selected_element_name: str) -> None:
    self.__terrain_repository.load(selected_element_name)
    self.__environment_service.set_environment()
    self._view_service.navigate_to(ViewUiConstants.PLAY_AGENT_SELECTION_SCREEN_IDENTIFIER)

  def get_previous_view_identifier(self) -> str:
    return ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER
