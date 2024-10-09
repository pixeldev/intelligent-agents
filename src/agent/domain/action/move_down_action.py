from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveDownAction(MoveAction):
  """
  Represents an action to move an agent down.

  Attributes:
    IDENTIFIER (str): A unique identifier for the move down action.
  """
  IDENTIFIER: str = 'move_down'

  def __init__(self) -> None:
    """
    Initializes a MoveDownAction instance with the identifier 'move_down'.
    """
    super().__init__(MoveDownAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Calculates the new coordinates after moving down.

    Args:
      agent (Agent): The agent performing the move action.
      steps (int): The number of steps to move down.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving down.
    """
    return MoveActionNewCoordinates(steps, 0, Direction.DOWN)
