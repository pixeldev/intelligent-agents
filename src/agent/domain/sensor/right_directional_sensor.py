from src.agent.domain.sensor.directional_sensor import DirectionalSensor


class RightDirectionalSensor(DirectionalSensor):
  """
  Sensor class for detecting rightward movement.

  Attributes:
      IDENTIFIER (str): A unique identifier for the sensor.
  """
  IDENTIFIER: str = 'right_directional'

  def __init__(self):
    """
    Initializes the RightDirectionalSensor with the identifier 'right_directional'.
    """
    super().__init__(RightDirectionalSensor.IDENTIFIER)

  def get_new_coordinates(self, x: int, y: int, i: int) -> tuple[int, int]:
    """
    Calculates new coordinates after moving right.

    Args:
        x (int): The current x-coordinate.
        y (int): The current y-coordinate.
        i (int): The distance to move right.

    Returns:
        tuple[int, int]: The new coordinates after moving right.
    """
    return x, y + i
