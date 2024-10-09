import json
import os
from typing import Optional

from src.environment.domain.terrain.terrain import Terrain


class TerrainRepository:
  """
  Class that handles loading and accessing terrain data.

  Attributes:
    __directory_path (str): The directory path where terrain files are stored.
    __terrain_dict (dict[int, Terrain]): A dictionary mapping terrain codes to Terrain objects.
  """

  def __init__(self, directory_path: str) -> None:
    """
    Initializes the TerrainRepository with an empty terrain_dict attribute.

    Args:
      directory_path (str): The directory path where terrain files are stored.
    """
    self.__directory_path: str = directory_path
    self.__terrain_dict: dict[int, Terrain] = {}

  def load(self, file_name: str) -> None:
    """
    Loads terrain data from the JSON file at the given path and stores it in the terrain_dict attribute.

    Args:
      file_name (str): The name of the file to load without the directory path.

    Raises:
      FileNotFoundError: If the file at the given path does not exist.
    """
    with open(f'{self.__directory_path}/{file_name}') as file:
      terrain_data = json.load(file)

    for terrain_code, terrain_data in terrain_data.items():
      self.__terrain_dict[int(terrain_code)] = Terrain(
        terrain_code,
        terrain_data['color'],
        terrain_data['display_name'],
        terrain_data['movement_costs'])

  def get_all_from_directory(self) -> list[str]:
    """
    Returns a list of all terrain display names.

    Returns:
      list[str]: A list of all terrain display names.
    """
    return os.listdir(self.__directory_path)

  def get_by_code(self, code: int) -> Optional[Terrain]:
    """
    Returns the Terrain object corresponding to the given code or None if the code is not found.

    Args:
      code (int): The code of the terrain to return.

    Returns:
      Optional[Terrain]: The Terrain object corresponding to the given code or None if the code is not found.
    """
    return self.__terrain_dict.get(code)

  def get_all(self) -> list[Terrain]:
    """
    Returns a list of all Terrain objects.

    Returns:
      list[Terrain]: A list of all Terrain objects.
    """
    return list(self.__terrain_dict.values())
