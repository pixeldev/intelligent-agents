from src.agent.domain.action.action import Action
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment


class TurnLeftAction(Action):
  """
  Represents an action where an agent turns left in the environment.

  Attributes:
      IDENTIFIER (str): The identifier for the turn left action.
  """

  IDENTIFIER: str = 'turn_left'

  def __init__(self):
    """
    Initializes a TurnLeftAction instance.
    """
    super().__init__(self.IDENTIFIER)

  def execute(self, agent: Agent, agent_action: ActionConfiguration, environment: Environment) -> None:
    """
    Executes the turn left action.

    Args:
        agent (Agent): The agent performing the action.
        agent_action (ActionConfiguration): The specific action configuration for the agent.
        environment (Environment): The environment in which the action is performed.
    """
    agent.set_direction(agent.get_direction().turn_left())
