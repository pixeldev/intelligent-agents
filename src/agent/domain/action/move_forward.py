from typing import Optional
from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Agent, Direction


class MoveForwardAction(MoveAction):
  """
  Represents an action to move an agent forward in its current direction.

  Attributes:
    IDENTIFIER (str): A unique identifier for the move forward action.
  """
  IDENTIFIER: str = 'move_forward'

  def __init__(self) -> None:
    """
    Initializes a MoveForwardAction instance with the identifier 'move_forward'.
    """
    super().__init__(MoveForwardAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Calculates the new coordinates after moving forward in the agent's current direction.

    Args:
      agent (Agent): The agent performing the move action.
      steps (int): The number of steps to move forward.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving forward, or None if the direction is unknown.
    """
    direction: Optional[Direction] = agent.get_direction()
    if direction is None:
      return None

    if direction == Direction.UP:
      return MoveActionNewCoordinates(0, -steps, direction)
    elif direction == Direction.DOWN:
      return MoveActionNewCoordinates(0, steps, direction)
    elif direction == Direction.LEFT:
      return MoveActionNewCoordinates(-steps, 0, direction)
    elif direction == Direction.RIGHT:
      return MoveActionNewCoordinates(steps, 0, direction)
    else:
      return None
