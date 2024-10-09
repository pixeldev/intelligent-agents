from src.agent.domain.action.action import Action
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment


class TurnRightAction(Action):
  """
  Represents an action where an agent turns right in the environment.

  Attributes:
      IDENTIFIER (str): The identifier for the turn right action.
  """

  IDENTIFIER: str = 'turn_right'

  def __init__(self):
    """
    Initializes a TurnRightAction instance.
    """
    super().__init__(TurnRightAction.IDENTIFIER)

  def execute(self, agent: Agent, agent_action: ActionConfiguration, environment: Environment) -> None:
    """
    Executes the turn right action.

    Args:
        agent (Agent): The agent performing the action.
        agent_action (ActionConfiguration): The specific action configuration for the agent.
        environment (Environment): The environment in which the action is performed.
    """
    agent.set_direction(agent.get_direction().turn_right())
