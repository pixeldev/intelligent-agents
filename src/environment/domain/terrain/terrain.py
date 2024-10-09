from typing import Optional


class Terrain:
  """
  Represents a type of terrain on the environment.

  Attributes:
    __code (int): The code associated with the terrain.
    __color (str): The color associated with the terrain.
    __display_name (str): The name of the terrain.
    __movement_costs_by_agent (dict[str, Optional[int]]): A dictionary mapping the cost of movement for each type of agent.
  """

  def __init__(self, code: int, color: str, display_name: str, movement_costs_by_agent: dict[str, Optional[int]]):
    """
    Initializes a Terrain instance.

    Args:
      code (int): The code associated with the terrain.
      display_name (str): The name of the terrain.
      color (str): The color associated with the terrain.
      movement_costs_by_agent (dict[str, Optional[int]]): A dictionary mapping the cost of movement for each type of agent.
    """
    self.__code: int = code
    self.__color: str = color
    self.__display_name: str = display_name
    self.__movement_costs_by_agent: dict[str, Optional[int]] = movement_costs_by_agent

  def get_code(self) -> int:
    """
    Returns the code associated with the terrain.

    Returns:
      int: The code associated with the terrain.
    """
    return self.__code

  def get_color(self) -> str:
    """
    Returns the color associated with the terrain.

    Returns:
      str: The color associated with the terrain.
    """
    return self.__color

  def get_display_name(self) -> str:
    """
    Returns the name of the terrain.

    Returns:
      str: The name of the terrain.
    """
    return self.__display_name

  def get_movement_cost(self, agent_name: str) -> Optional[int]:
    """
    Returns the movement cost for a given type of agent.

    Args:
      agent_name (str): The name of the agent.

    Returns:
      Optional[int]: The movement cost for the given agent, or None if the agent cannot traverse the terrain.
    """
    return self.__movement_costs_by_agent.get(agent_name)

  def __str__(self) -> str:
    """
    Returns a string representation of the Terrain instance.

    Returns:
      str: A string representation of the Terrain instance.
    """
    return f'Terrain {self.__display_name} (code: {self.__code}, color: {self.__color})'
