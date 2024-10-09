from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveLeftAction(MoveAction):
  """
  Represents an action to move an agent to the left.

  Attributes:
    IDENTIFIER (str): A unique identifier for the move left action.
  """
  IDENTIFIER: str = 'move_left'

  def __init__(self) -> None:
    """
    Initializes a MoveLeftAction instance with the identifier 'move_left'.
    """
    super().__init__(MoveLeftAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Calculates the new coordinates after moving left.

    Args:
      agent (Agent): The agent performing the move action.
      steps (int): The number of steps to move left.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving left.
    """
    return MoveActionNewCoordinates(0, -steps, Direction.LEFT)
