from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor import Sensor, SensorResult
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.environment.domain.environment import Environment


class MergedSensor(Sensor):
  def __init__(self, identifier: str, sensors: list[Sensor]):
    super().__init__(identifier)
    self.__sensors: list[Sensor] = sensors

  def detect(self, agent: Agent, sensor_configuration: SensorConfiguration, environment: Environment) -> SensorResult:
    sensor_result: SensorResult = SensorResult.SUCCESS
    pass_trough = sensor_configuration.can_pass_trough()
    for sensor in self.__sensors:
      sensor_result = sensor.detect(agent, sensor_configuration, environment)
      if sensor_result == SensorResult.HIT_OBSTACLE and not pass_trough:
        return sensor_result
    return sensor_result
