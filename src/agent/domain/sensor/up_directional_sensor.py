from src.agent.domain.sensor.directional_sensor import DirectionalSensor


class UpDirectionalSensor(DirectionalSensor):
  """
  Sensor class for detecting upward movement.

  Attributes:
      IDENTIFIER (str): A unique identifier for the sensor.
  """
  IDENTIFIER: str = 'up_directional'

  def __init__(self):
    """
    Initializes the UpDirectionalSensor with the identifier 'up_directional'.
    """
    super().__init__(UpDirectionalSensor.IDENTIFIER)

  def get_new_coordinates(self, x: int, y: int, i: int) -> tuple[int, int]:
    """
    Calculates new coordinates after moving up.

    Args:
        x (int): The current x-coordinate.
        y (int): The current y-coordinate.
        i (int): The distance to move up.

    Returns:
        tuple[int, int]: The new coordinates after moving up.
    """
    return x - i, y
