import flet

from src.environment.application.environment_agent_service import EnvironmentAgentService
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map_repository import MapRepository
from ui.creation.creation_main_screen_view_ui import CreationMainScreenViewUi
from ui.creation.creation_terrain_selection_view_ui import CreationTerrainSelectionViewUi
from ui.edition.edition_main_screen_view_ui import EditionMainScreenViewUi
from ui.edition.edition_map_selection_view_ui import EditionMapSelectionViewUi
from ui.main_screen_view_ui import MainScreenViewUi
from ui.play.play_agent_finish_position_selection_view_ui import PlayAgentFinishPositionSelectionViewUi
from ui.play.play_agent_position_selection_view_ui import PlayAgentPositionSelectionViewUi
from ui.play.play_agent_selection_view_ui import PlayAgentSelectionViewUi
from ui.play.play_game_actions_view_ui import PlayGameActionsViewUi
from ui.play.play_game_sensors_view_ui import PlayGameSensorsViewUi
from ui.play.play_game_view_ui import PlayGameViewUi
from ui.play.play_main_screen_view_ui import PlayMainScreenViewUi
from ui.play.play_map_selection_view_ui import PlayMapSelectionViewUi
from ui.play.play_terrain_selection_view_ui import PlayTerrainSelectionViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class AppUi:
  def __init__(self, environment_agent_service: EnvironmentAgentService, environment_service: EnvironmentService, map_repository: MapRepository, terrain_repository: TerrainRepository):
    self.__environment_agent_service = environment_agent_service
    self.__environment_service = environment_service
    self.__map_repository = map_repository
    self.__terrain_repository = terrain_repository

  def start(self, page: flet.Page):
    page.title = "Menú Principal"
    page.window.full_screen = True
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    view_service: ViewUiService = ViewUiService(page)

    view_service.register(MainScreenViewUi(view_service))
    view_service.register(PlayMainScreenViewUi(view_service))
    view_service.register(PlayMapSelectionViewUi(self.__map_repository, view_service))
    view_service.register(PlayTerrainSelectionViewUi(self.__environment_service, self.__terrain_repository, view_service))
    view_service.register(PlayAgentSelectionViewUi(self.__environment_service, view_service))
    view_service.register(PlayAgentPositionSelectionViewUi(self.__environment_service, view_service))
    view_service.register(PlayAgentFinishPositionSelectionViewUi(self.__environment_service, view_service))
    view_service.register(PlayGameViewUi(self.__environment_service, view_service))
    view_service.register(PlayGameSensorsViewUi(self.__environment_agent_service, self.__environment_service, view_service))
    view_service.register(PlayGameActionsViewUi(self.__environment_agent_service, self.__environment_service, view_service))
    view_service.register(EditionMainScreenViewUi(view_service))
    view_service.register(EditionMapSelectionViewUi(self.__map_repository, view_service))
    view_service.register(CreationMainScreenViewUi(view_service))
    view_service.register(CreationTerrainSelectionViewUi(self.__terrain_repository, view_service))

    view_service.navigate_to(ViewUiConstants.MAIN_SCREEN_IDENTIFIER)
