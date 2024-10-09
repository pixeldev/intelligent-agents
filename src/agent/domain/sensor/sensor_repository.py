from typing import Optional

from src.agent.domain.sensor.sensor import Sensor


class SensorRepository:
  """
  A repository for managing Sensor objects.

  Attributes:
    __sensors (dict[str, Sensor]): A dictionary to store sensors with their identifiers as keys.
  """

  def __init__(self):
    """
    Initializes a SensorRepository instance.
    """
    self.__sensors: dict[str, Sensor] = {}

  def add_sensor(self, sensor: Sensor):
    """
    Adds a sensor to the repository.

    Args:
      sensor (Sensor): The sensor to add.
    """
    self.__sensors[sensor.get_identifier()] = sensor

  def add_sensors(self, *sensors: Sensor):
    """
    Adds a list of sensors to the repository.

    Args:
      sensors (Sensor): The sensors to add.
    """
    for sensor in sensors:
      self.add_sensor(sensor)

  def get_sensor(self, identifier: str) -> Optional[Sensor]:
    """
    Retrieves a sensor by its identifier.

    Args:
      identifier (str): The identifier of the sensor to retrieve.

    Returns:
      Optional[Sensor]: The sensor with the given identifier, or None if not found.
    """
    return self.__sensors.get(identifier)

  def get_sensors(self) -> list[Sensor]:
    """
    Retrieves all sensors in the repository.

    Returns:
      list[Sensor]: A list of all sensors.
    """
    return list(self.__sensors.values())
