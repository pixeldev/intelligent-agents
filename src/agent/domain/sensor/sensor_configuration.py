class SensorConfiguration:
  """
  Represents a sensor attached to an agent.

  Attributes:
    __description (str): The description of the sensor.
    __display_name (str): The display name of the sensor.
    __identifier (str): The unique identifier for the sensor.
    __pass_trough (bool): A flag indicating if the sensor can pass through obstacles.
    __radius (int): The radius of the sensor.
  """

  def __init__(self, description: str, display_name: str, identifier: str, pass_trough: bool, radius: int):
    """
    Initializes a SensorConfiguration instance.

    Args:
      description (str): The description of the sensor.
      identifier (str): The unique identifier for the sensor.
      pass_trough (bool): A flag indicating if the sensor can pass through obstacles.
      radius (int): The radius of the sensor.

    Raises:
      ValueError: If the radius is less than 1.
    """
    if radius < 1:
      raise ValueError('The radius must be greater than 0')
    self.__description = description
    self.__display_name = display_name
    self.__identifier = identifier
    self.__pass_trough = pass_trough
    self.__radius = radius

  def get_description(self) -> str:
    """
    Gets the description of the sensor.

    Returns:
      str: The description of the sensor.
    """
    return self.__description

  def get_name(self) -> str:
    """
    Gets the display name of the sensor.

    Returns:
      str: The display name of the sensor.
    """
    return self.__display_name

  def get_identifier(self) -> str:
    """
    Gets the identifier of the sensor.

    Returns:
      str: The unique identifier of the sensor.
    """
    return self.__identifier

  def get_radius(self) -> int:
    """
    Gets the radius of the sensor.

    Returns:
      int: The radius of the sensor.
    """
    return self.__radius

  def can_pass_trough(self) -> bool:
    """
    Checks if the sensor can pass through obstacles.

    Returns:
      bool: True if the sensor can pass through obstacles, False otherwise.
    """
    return self.__pass_trough
