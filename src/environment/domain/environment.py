from typing import Optional

from src.agent.domain.agent import Agent
from src.environment.domain.cell.cell import Cell


class Environment:
  """
  Represents the environment in which agents operate.

  Attributes:
    __agents (list[Agent]): The list of agents in the environment.
    __discovered_map (list[list[bool]]): The map of discovered cells.
    __grid (list[list[Cell]]): The grid representing the environment.
    __rows (int): The number of rows in the environment.
    __columns (int): The number of columns in the environment.
  """

  def __init__(self, agents: list[Agent], discovered_map: list[list[bool]], grid: list[list[Cell]], rows: int, columns: int):
    """
    Initializes an Environment instance.

    Args:
      agents (list[Agent]): The list of agents in the environment.
      discovered_map (list[list[bool]]): The map of discovered cells.
      grid (list[list[Cell]]): The grid representing the environment.
      rows (int): The number of rows in the environment.
      columns (int): The number of columns in the environment
    """
    self.__agents: list[Agent] = agents
    self.__selected_agent: Optional[Agent] = None
    self.__discovered_map: list[list[bool]] = discovered_map
    self.__grid: list[list[Cell]] = grid
    self.__rows: int = rows
    self.__columns: int = columns

  def get_selected_agent(self) -> Optional[Agent]:
    """
    Returns the selected agent.

    Returns:
      Optional[Agent]: The selected agent.
    """
    return self.__selected_agent

  def set_selected_agent(self, agent: Optional[Agent]):
    """
    Sets the selected agent.

    Args:
      agent (Optional[Agent]): The agent to be selected.
    """
    self.__selected_agent = agent

  def get_agents(self) -> list[Agent]:
    """
    Returns the list of agents in the environment.

    Returns:
      list[Agent]: The list of agents.
    """
    return self.__agents

  def add_agent(self, agent: Agent):
    """
    Adds an agent to the environment.

    Args:
      agent (Agent): The agent to be added.
    """
    self.__agents.append(agent)
    self.__discovered_map[agent.get_x()][agent.get_y()] = True

  def get_cell(self, x: int, y: int) -> Optional[Cell]:
    """
    Returns the state of the terrain at a specific position.

    Args:
      x (int): The x-coordinate of the position.
      y (int): The y-coordinate of the position.

    Returns:
      Cell: The cell at the specified position.
    """
    if y < 0 or y >= self.__rows or x < 0 or x >= self.__columns:
      return None
    return self.__grid[y][x]

  def update_discovered_map(self, x: int, y: int, value: bool):
    """
    Updates the discovered map at a specific position.

    Args:
      x (int): The x-coordinate of the position to update.
      y (int): The y-coordinate of the position to update.
      value (bool): The new value for the position.
    """
    self.__discovered_map[y][x] = value

  def get_discovered_map(self) -> list[list[bool]]:
    """
    Returns the discovered map.

    Returns:
      list[list[bool]]: The discovered map.
    """
    return self.__discovered_map

  def is_discovered(self, x: int, y: int) -> bool:
    """
    Checks if a cell has been discovered.

    Args:
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.

    Returns:
      bool: True if the cell has been discovered, False otherwise.
    """
    return self.__discovered_map[y][x]

  def update_state(self, x: int, y: int, new_value: Cell):
    """
    Changes the state of the environment at a position and updates both the global and agents' maps.

    Args:
      x (int): The x-coordinate of the position to update.
      y (int): The y-coordinate of the position to update.
      new_value (Cell): The new value for the position.
    """
    self.__grid[y][x] = new_value

  def is_obstacle_for(self, agent: Agent, x: int, y: int) -> Optional[bool]:
    """
    Checks if a cell is an obstacle for an agent.

    Args:
      agent (Agent): The agent to check the cell for.
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.

    Returns:
      bool: True if the cell is an obstacle for the agent, False otherwise.
    """
    cell: Optional[Cell] = self.get_cell(x, y)
    if cell is None:
      return None
    return cell.get_movement_cost_for(agent.get_name()) is None

  def get_rows(self) -> int:
    """
    Returns the number of rows in the environment.

    Returns:
      int: The number of rows.
    """
    return self.__rows

  def get_columns(self) -> int:
    """
    Returns the number of columns in the environment.

    Returns:
      int: The number of columns.
    """
    return self.__columns

  def is_agent_in_position(self, x: int, y: int) -> bool:
    """
    Checks if an agent is in a specific position.

    Args:
      x (int): The x-coordinate of the position.
      y (int): The y-coordinate of the position.

    Returns:
      bool: True if an agent is in the position, False otherwise.
    """
    for agent in self.__agents:
      if agent.get_x() == x and agent.get_y() == y:
        return True
    return False

  def print_discovered_map(self):
    """
    Prints the discovered parts of the environment.
    """
    # Print the top border of the map
    top_border = '┌' + '┬'.join(['─' * 3] * self.__columns) + '┐'
    print(top_border)

    for y in range(self.__rows):
      # Print each row with cell values
      row = '│'
      for x in range(self.__columns):
        if self.is_agent_in_position(x, y):
          cell = ' \033[43m \033[0m '
        elif self.__discovered_map[y][x]:
          cell = ' \033[42m \033[0m '
        else:
          cell = ' \033[40m \033[0m '
        row += cell + '│'
      print(row)

      # Print row separator if not the last row
      if y != self.__rows - 1:
        row_separator = '├' + '┼'.join(['─' * 3] * self.__columns) + '┤'
        print(row_separator)

    # Print the bottom border of the map
    bottom_border = '└' + '┴'.join(['─' * 3] * self.__columns) + '┘'
    print(bottom_border)
