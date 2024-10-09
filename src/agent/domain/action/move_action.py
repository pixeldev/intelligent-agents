from abc import ABC, abstractmethod
from typing import Optional
from src.agent.domain.action.action import Action, ActionResult
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent, Direction
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment


class MoveActionNewCoordinates:
  """
  Represents the new coordinates after a move action.

  Attributes:
    __dx (int): The change in the x-coordinate.
    __dy (int): The change in the y-coordinate.
    __direction (Direction): The direction of the move.
  """

  def __init__(self, dx: int, dy: int, direction: Direction):
    """
    Initializes a MoveActionNewCoordinates instance.

    Args:
      dx (int): The change in the x-coordinate.
      dy (int): The change in the y-coordinate.
      direction (Direction): The direction of the move.
    """
    self.__dx = dx
    self.__dy = dy
    self.__direction = direction

  def get_dx(self) -> int:
    """
    Returns the change in the x-coordinate.

    Returns:
      int: The change in the x-coordinate.
    """
    return self.__dx

  def get_dy(self) -> int:
    """
    Returns the change in the y-coordinate.

    Returns:
      int: The change in the y-coordinate.
    """
    return self.__dy

  def get_direction(self) -> Direction:
    """
    Returns the direction of the move.

    Returns:
      Direction: The direction of the move.
    """
    return self.__direction


class MoveAction(Action, ABC):
  """
  Base class for move actions.

  Attributes:
    __identifier (str): The identifier of the action.
  """

  def __init__(self, identifier: str) -> None:
    """
    Initializes a MoveAction instance.

    Args:
      identifier (str): The identifier of the action.
    """
    super().__init__(identifier)

  @abstractmethod
  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Returns the new coordinates after moving a certain number of steps.

    Args:
      agent (Agent): The agent performing the action.
      steps (int): The number of steps to move.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving.
    """
    pass

  def execute(self, agent: Agent, agent_action: ActionConfiguration, environment: Environment) -> ActionResult:
    """
    Executes the move action.

    Args:
      agent (Agent): The agent performing the action.
      agent_action (ActionConfiguration): The specific action configuration for the agent.
      environment (Environment): The environment in which the action is performed.

    Returns:
      ActionResult: The result of the action.
    """
    steps: int = agent_action.get_property('steps')
    if type(steps) is not int or steps < 1:
      return ActionResult.INVALID_PROPERTY

    new_coordinates: Optional[MoveActionNewCoordinates] = self.get_new_coordinates(agent, steps)
    if new_coordinates is None:
      return ActionResult.UNKNOWN_DIRECTION

    x: int = agent.get_x() + new_coordinates.get_dx()
    y: int = agent.get_y() + new_coordinates.get_dy()
    if not agent.is_known(x, y):
      return ActionResult.UNKNOWN_CELL

    cell: Optional[Cell] = environment.get_cell(x, y)
    if cell is None:
      return ActionResult.OUT_OF_BOUNDS

    movement_cost: Optional[int] = cell.get_movement_cost_for(agent.get_name())
    if movement_cost is None:
      return ActionResult.HIT_OBSTACLE

    agent.set_direction(new_coordinates.get_direction())
    agent.update_position(x, y)
    agent.increase_accumulated_movement_cost(movement_cost)
    agent.increase_steps()

    if agent.is_at_finish_position():
      return ActionResult.GOAL_REACHED
    return ActionResult.SUCCESS
