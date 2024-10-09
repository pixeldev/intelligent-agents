class ActionConfiguration:
  """
  Represents the configuration for an action that an agent can perform.

  Attributes:
    __description (str): The description of the action.
    __display_name (str): The display name of the action.
    __identifier (str): The identifier of the action.
    __properties (dict[str, any]): The properties of the action.
  """

  def __init__(self, description: str, display_name: str, identifier: str, properties: dict[str, any]):
    """
    Initializes an ActionConfiguration instance.

    Args:
      description (str): The description of the action.
      display_name (str): The display name of the action.
      identifier (str): The identifier of the action.
      properties (dict[str, any]): The properties of the action.
    """
    self.__description: str = description
    self.__display_name: str = display_name
    self.__identifier: str = identifier
    self.__properties: dict[str, any] = properties

  def get_description(self) -> str:
    """
    Returns the description of the action.

    Returns:
      str: The description of the action.
    """
    return self.__description

  def get_name(self) -> str:
    """
    Returns the display name of the action.

    Returns:
      str: The display name of the action.
    """
    return self.__display_name

  def get_identifier(self) -> str:
    """
    Returns the identifier of the action.

    Returns:
      str: The identifier of the action.
    """
    return self.__identifier

  def get_property(self, key: str) -> any:
    """
    Returns the property with the specified key.

    Args:
      key (str): The key of the property to retrieve.

    Returns:
      any: The value of the property associated with the specified key.
    """
    return self.__properties[key]
