from abc import ABC, abstractmethod
from typing import Optional
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor import Sensor, SensorResult
from src.environment.domain.environment import Environment


class DirectionalSensor(Sensor, ABC):
  """
  Represents a sensor that detects the terrain type in a specific direction around the agent.
  """

  @abstractmethod
  def get_new_coordinates(self, x: int, y: int, i: int) -> tuple[int, int]:
    """
    Gets the new coordinates based on the direction of the sensor.

    Args:
      x (int): The current x-coordinate of the agent.
      y (int): The current y-coordinate of the agent.
      i (int): The step in the direction.

    Returns:
      tuple[int, int]: The new coordinates.
    """
    pass

  def detect(self, agent: Agent, sensor_configuration: SensorConfiguration, environment: Environment) -> SensorResult:
    """
    Detects the terrain type in the cells in the specific direction of the agent, updating its individual knowledge and the global map of the environment.

    Args:
      agent (Agent): The agent that will detect the terrain type.
      sensor_configuration (SensorConfiguration): The specific sensor configuration for the agent.
      environment (Environment): The environment in which the agent operates.

    Returns:
      SensorResult: The result of the sensor detection.
    """
    x: int = agent.get_x()
    y: int = agent.get_y()
    pass_trough: bool = sensor_configuration.can_pass_trough()
    for i in range(1, sensor_configuration.get_radius() + 1):
      new_x, new_y = self.get_new_coordinates(x, y, i)
      if agent.is_known(new_x, new_y):
        continue
      obstacle: Optional[bool] = environment.is_obstacle_for(agent, new_x, new_y)
      if obstacle is None:
        return SensorResult.OUT_OF_BOUNDS
      agent.set_known(new_x, new_y)
      environment.update_discovered_map(new_x, new_y, True)
      if obstacle and not pass_trough:
        return SensorResult.HIT_OBSTACLE
    return SensorResult.SUCCESS
