from typing import Optional

from src.environment.domain.terrain.terrain import Terrain


class Cell:
  """
  Entity that represents a cell in the map.

  Attributes:
    __terrain (Terrain): The terrain type of the cell.
    __x (int): The x-coordinate of the cell.
    __y (int): The y-coordinate of the cell.
  """

  def __init__(self, terrain: Terrain, x: int, y: int):
    """
    Initializes a Cell instance.

    Args:
      terrain (Terrain): The terrain type of the cell.
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.
    """
    self.__terrain: Terrain = terrain
    self.__x: int = x
    self.__y: int = y

  def get_x(self) -> int:
    """
    Gets the x-coordinate of the cell.

    Returns:
      int: The x-coordinate of the cell.
    """
    return self.__x

  def get_y(self) -> int:
    """
    Gets the y-coordinate of the cell.

    Returns:
      int: The y-coordinate of the cell.
    """
    return self.__y

  def get_terrain(self) -> Terrain:
    """
    Gets the terrain type of the cell.

    Returns:
      Terrain: The terrain type of the cell.
    """
    return self.__terrain

  def set_terrain(self, terrain: Terrain):
    """
    Sets the terrain type of the cell.

    Args:
      terrain (Terrain): The new terrain type of the cell.
    """
    self.__terrain = terrain

  def get_movement_cost_for(self, agent_name: str) -> Optional[int]:
    """
    Checks if the cell is walkable.

    Returns:
      bool: True if the cell is walkable, False otherwise.
    """
    return self.__terrain.get_movement_cost(agent_name)

  def __str__(self) -> str:
    """
    Returns a string representation of the cell.

    Returns:
      str: A string representation of the cell.
    """
    return f"Cell(x={self.__x}, y={self.__y}, terrain={self.__terrain})"
