from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveUpAction(MoveAction):
  """
  Represents an action to move an agent up.

  Attributes:
    IDENTIFIER (str): A unique identifier for the move up action.
  """
  IDENTIFIER: str = 'move_up'

  def __init__(self) -> None:
    """
    Initializes a MoveUpAction instance with the identifier 'move_up'.
    """
    super().__init__(MoveUpAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    """
    Calculates the new coordinates after moving up.

    Args:
      agent (Agent): The agent performing the move action.
      steps (int): The number of steps to move up.

    Returns:
      Optional[MoveActionNewCoordinates]: The new coordinates after moving up.
    """
    return MoveActionNewCoordinates(-steps, 0, Direction.UP)
