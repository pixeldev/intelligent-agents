from src.agent.domain.sensor.directional_sensor import DirectionalSensor


class LeftDirectionalSensor(DirectionalSensor):
  """
  Sensor class for detecting leftward movement.

  Attributes:
      IDENTIFIER (str): A unique identifier for the sensor.
  """
  IDENTIFIER: str = 'left_directional'

  def __init__(self):
    """
    Initializes the LeftDirectionalSensor with the identifier 'left_directional'.
    """
    super().__init__(LeftDirectionalSensor.IDENTIFIER)

  def get_new_coordinates(self, x: int, y: int, i: int) -> tuple[int, int]:
    """
    Calculates new coordinates after moving left.

    Args:
        x (int): The current x-coordinate.
        y (int): The current y-coordinate.
        i (int): The distance to move left.

    Returns:
        tuple[int, int]: The new coordinates after moving left.
    """
    return x, y - 1
