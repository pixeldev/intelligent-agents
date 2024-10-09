from typing import Optional

from src.agent.domain.default_agents import DefaultAgents
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from src.environment.domain.terrain.terrain import Terrain
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map import Map
from src.map.domain.map_repository import MapRepository


class EnvironmentService:
  """
  Provides services for managing and interacting with the Environment class.

  Attributes:
    __terrain_repository (TerrainRepository): Repository for retrieving terrain information.
  """

  def __init__(self, map_repository: MapRepository, terrain_repository: TerrainRepository):
    """
    Initializes an EnvironmentService instance.

    Args:
      terrain_repository (TerrainRepository): Repository for retrieving terrain information.
    """
    self.__environment: Optional[Environment] = None
    self.__map_repository: MapRepository = map_repository
    self.__terrain_repository: TerrainRepository = terrain_repository

  def get_environment(self) -> Optional[Environment]:
    """
    Returns the environment instance.

    Returns:
      Optional[Environment]: The environment instance.
    """
    return self.__environment

  def create_cells_from_map(self, map: Map) -> list[list[Cell]]:
    """
    Creates a grid of cells from a map.

    Args:
      map (Map): The map from which to create cells.

    Returns:
      list[list[Cell]]: A 2D list of cells created from the map.

    Raises:
      ValueError: If a terrain code in the map does not correspond to any terrain in the repository.
    """
    cells: list[list[Cell]] = []
    for row in range(map.get_rows()):
      cells.append([])
      for column in range(map.get_columns()):
        terrain: Optional[Terrain] = self.__terrain_repository.get_by_code(map.get_cell(row, column))
        if terrain is None:
          raise ValueError(f'Terrain with code {map.get_cell(row, column)} not found.')
        cells[row].append(Cell(terrain, row, column))
    return cells

  def set_environment(self) -> None:
    """
    Creates an environment instance from the selected map and terrain.

    Raises:
      ValueError: If no map is selected.
    """
    map: Optional[Map] = self.__map_repository.get_map()
    if map is None:
      raise ValueError("No map selected.")
    cells: list[list[Cell]] = self.create_cells_from_map(map)
    rows: int = map.get_rows()
    columns: int = map.get_columns()
    discovered_map: list[list[bool]] = [[False for _ in range(rows)] for _ in range(columns)]
    self.__environment = Environment([], discovered_map, cells, rows, columns)
    self.__environment.add_agent(DefaultAgents.create_agent('human', columns, rows))
    self.__environment.add_agent(DefaultAgents.create_agent('monkey', columns, rows))
    self.__environment.add_agent(DefaultAgents.create_agent('sasquatch', columns, rows))
    self.__environment.add_agent(DefaultAgents.create_agent('octopus', columns, rows))
