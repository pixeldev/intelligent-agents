from abc import abstractmethod
from enum import Enum

from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment


class ActionResult(Enum):
  """
  Enum representing the possible results of an action.

  Attributes:
    SUCCESS (int): The action was successful.
    OUT_OF_BOUNDS (int): The action went out of bounds.
    HIT_OBSTACLE (int): The action hit an obstacle.
    UNKNOWN_CELL (int): The action encountered an unknown cell.
    UNKNOWN_DIRECTION (int): The action encountered an unknown direction.
    INVALID_PROPERTY (int): The action had an invalid property.
    GOAL_REACHED (int): The action reached the goal.
  """
  SUCCESS = 1
  OUT_OF_BOUNDS = 2
  HIT_OBSTACLE = 3
  UNKNOWN_CELL = 4
  UNKNOWN_DIRECTION = 5
  INVALID_PROPERTY = 6
  GOAL_REACHED = 7


class Action:
  """
  Represents an action that an agent can perform.

  Attributes:
    __identifier (str): The identifier of the action.
  """

  def __init__(self, identifier: str):
    """
    Initializes an Action instance.

    Args:
      identifier (str): The identifier of the action.
    """
    self.__identifier = identifier

  def get_identifier(self) -> str:
    """
    Returns the action identifier.

    Returns:
      str: The action identifier.
    """
    return self.__identifier

  @abstractmethod
  def execute(self, agent: Agent, agent_action: ActionConfiguration, environment: Environment) -> ActionResult:
    """
    Executes the action.

    Args:
      agent (Agent): The agent performing the action.
      agent_action (ActionConfiguration): The specific action configuration for the agent.
      environment (Environment): The environment in which the action is performed.

    Returns:
      ActionResult: The result of the action.
    """
    raise NotImplementedError('This method should be implemented by the subclass.')
