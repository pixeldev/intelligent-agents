from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveRightAction(MoveAction):
  """
  Represents an action to move an agent to the right.

  Attributes:
    IDENTIFIER (str): A unique identifier for the move right action.
  """
  IDENTIFIER: str = 'move_right'

  def __init__(self) -> None:
    """
    Initializes a MoveRightAction instance with the identifier 'move_right'.
    """
    super().__init__(MoveRightAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Calculates the new coordinates after moving right.

    Args:
      agent (Agent): The agent performing the move action.
      steps (int): The number of steps to move right.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving right.
    """
    return MoveActionNewCoordinates(0, steps, Direction.RIGHT)
