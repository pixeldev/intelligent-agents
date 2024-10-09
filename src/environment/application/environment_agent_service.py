from abc import ABC
from enum import Enum
from typing import Optional

from src.agent.domain.action.action import Action, ActionResult
from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor import Sensor, SensorResult
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor_repository import SensorRepository
from src.environment.domain.environment import Environment


class ResultCode(Enum):
  """
  Enum representing the result codes for actions and sensors.

  Attributes:
    SUCCESS (int): Indicates the action or sensor execution was successful.
    NOT_FOUND_IN_AGENT (int): Indicates the action or sensor was not found in the agent.
    NOT_FOUND_IN_REPOSITORY (int): Indicates the action or sensor was not found in the repository.
    FAILED (int): Indicates the action or sensor execution failed.
  """
  SUCCESS = 1
  NOT_FOUND_IN_AGENT = 2
  NOT_FOUND_IN_REPOSITORY = 3
  FAILED = 4


class Result(ABC):
  """
  Abstract base class for results of actions and sensors.

  Attributes:
    result_code (ResultCode): The result code of the action or sensor execution.
  """

  def __init__(self, result_code: ResultCode):
    """
    Initializes a Result instance.

    Args:
      result_code (ResultCode): The result code of the action or sensor execution.
    """
    self.result_code = result_code

  def get_code(self) -> ResultCode:
    """
    Gets the result code.

    Returns:
      ResultCode: The result code of the action or sensor execution.
    """
    return self.result_code


class ExecuteActionResult(Result):
  """
  Represents the result of executing an action.

  Attributes:
    __action_result (Optional[ActionResult]): The result of the action execution.
  """

  def __init__(self, result_code: ResultCode, action_result: Optional[ActionResult]):
    """
    Initializes an ExecuteActionResult instance.

    Args:
      result_code (ResultCode): The result code of the action execution.
      action_result (Optional[ActionResult]): The result of the action execution.
    """
    super().__init__(result_code)
    self.__action_result = action_result

  def get_action_result(self) -> Optional[ActionResult]:
    """
    Gets the action result.

    Returns:
      Optional[ActionResult]: The result of the action execution.
    """
    return self.__action_result


class ExecuteSensorResult(Result):
  """
  Represents the result of executing a sensor.

  Attributes:
    __sensor_result (Optional[SensorResult]): The result of the sensor execution.
  """

  def __init__(self, result_code: ResultCode, sensor_result: Optional[SensorResult]):
    """
    Initializes an ExecuteSensorResult instance.

    Args:
      result_code (ResultCode): The result code of the sensor execution.
      sensor_result (Optional[SensorResult]): The result of the sensor execution.
    """
    super().__init__(result_code)
    self.__sensor_result = sensor_result

  def get_sensor_result(self) -> Optional[SensorResult]:
    """
    Gets the sensor result.

    Returns:
      Optional[SensorResult]: The result of the sensor execution.
    """
    return self.__sensor_result


class EnvironmentAgentService:
  """
  Service class for managing agent actions and sensors in an environment.

  Attributes:
    __action_repository (ActionRepository): Repository for retrieving actions.
    __sensor_repository (SensorRepository): Repository for retrieving sensors.
  """

  def __init__(self, action_repository: ActionRepository, sensor_repository: SensorRepository):
    """
    Initializes an EnvironmentAgentService instance.

    Args:
      action_repository (ActionRepository): Repository for retrieving actions.
      sensor_repository (SensorRepository): Repository for retrieving sensors.
    """
    self.__action_repository = action_repository
    self.__sensor_repository = sensor_repository

  def execute_action(self, agent: Agent, environment: Environment, action_configuration: ActionConfiguration) -> ExecuteActionResult:
    """
    Executes an action for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the action.
      environment (Environment): The environment in which the agent will execute the action.
      action_configuration (str): The action configuration to be executed.

    Returns:
      ExecuteActionResult: The result of the action execution.
    """
    action: Action = self.__action_repository.get_action(action_configuration.get_identifier())
    if action is None:
      return ExecuteActionResult(ResultCode.NOT_FOUND_IN_REPOSITORY, None)
    action_result: ActionResult = action.execute(agent, action_configuration, environment)
    if action_result is not ActionResult.SUCCESS:
      return ExecuteActionResult(ResultCode.FAILED, action_result)
    return ExecuteActionResult(ResultCode.SUCCESS, action_result)

  def execute_action_from_identifier(self, agent: Agent, environment: Environment, action_identifier: str) -> ExecuteActionResult:
    """
    Executes an action for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the action.
      environment (Environment): The environment in which the agent will execute the action.
      action_identifier (str): The identifier of the action to be executed.

    Returns:
      ExecuteActionResult: The result of the action execution.
    """
    action_configuration: Optional[ActionConfiguration] = agent.get_action(action_identifier)
    if action_configuration is None:
      return ExecuteActionResult(ResultCode.NOT_FOUND_IN_AGENT, None)
    return self.execute_action(agent, environment, action_configuration)

  def execute_sensor_from_identifier(self, agent: Agent, environment: Environment, sensor_identifier: str) -> ExecuteSensorResult:
    """
    Executes a sensor for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the sensor.
      environment (Environment): The environment in which the agent will execute the sensor.
      sensor_identifier (str): The identifier of the sensor to be executed.

    Returns:
      ExecuteSensorResult: The result of the sensor execution.
    """
    sensor_configuration: Optional[SensorConfiguration] = agent.get_sensor(sensor_identifier)
    if sensor_configuration is None:
      return ExecuteSensorResult(ResultCode.NOT_FOUND_IN_AGENT, None)
    return self.execute_sensor(agent, environment, sensor_configuration)

  def execute_sensor(self, agent: Agent, environment: Environment, sensor_configuration: SensorConfiguration) -> ExecuteSensorResult:
    """
    Executes a sensor for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the sensor.
      environment (Environment): The environment in which the agent will execute the sensor.
      sensor_configuration (str): The sensor configuration to be executed.

    Returns:
      ExecuteSensorResult: The result of the sensor execution.
    """
    sensor: Sensor = self.__sensor_repository.get_sensor(sensor_configuration.get_identifier())
    if sensor is None:
      return ExecuteSensorResult(ResultCode.NOT_FOUND_IN_REPOSITORY, None)
    sensor_result: SensorResult = sensor.detect(agent, sensor_configuration, environment)
    if sensor_result is not SensorResult.SUCCESS:
      return ExecuteSensorResult(ResultCode.FAILED, sensor_result)
    return ExecuteSensorResult(ResultCode.SUCCESS, sensor_result)
