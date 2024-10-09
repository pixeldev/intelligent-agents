from src.agent.domain.sensor.directional_sensor import DirectionalSensor


class DownDirectionalSensor(DirectionalSensor):
  """
  Sensor class for detecting downward movement.

  Attributes:
      IDENTIFIER (str): A unique identifier for the sensor.
  """
  IDENTIFIER: str = 'down_directional'

  def __init__(self):
    """
    Initializes the DownDirectionalSensor with the identifier 'down_directional'.
    """
    super().__init__(DownDirectionalSensor.IDENTIFIER)

  def get_new_coordinates(self, x: int, y: int, i: int) -> tuple[int, int]:
    """
    Calculates new coordinates after moving down.

    Args:
        x (int): The current x-coordinate.
        y (int): The current y-coordinate.
        i (int): The distance to move down.

    Returns:
        tuple[int, int]: The new coordinates after moving down.
    """
    return x + 1, y
