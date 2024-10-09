class KnownCell:
  """
  Represents a cell known by the agent, which can have various flags associated with it.

  Attributes:
    __flags (list[str]): The list of flags associated with the cell.
  """

  def __init__(self, flags: list[str]):
    """
    Initializes a KnownCell instance.

    Args:
      flags (list[str]): The list of flags associated with the cell.
    """
    self.__flags: list[str] = flags

  def add_flags(self, flags: list[str]) -> bool:
    """
    Adds a flag to the cell if it is not already present.

    Args:
      flags (str): The flags to be added.

    Returns:
      bool: True if the flag was added, False if it was already present.
    """
    for flag in flags:
      if flag not in self.__flags:
        self.__flags.append(flag)
      else:
        return False
    return True

  def remove_flag(self, flag: str) -> bool:
    """
    Removes a flag from the cell if it is present.

    Args:
      flag (str): The flag to be removed.

    Returns:
      bool: True if the flag was removed, False if it was not present.
    """
    if flag in self.__flags:
      self.__flags.remove(flag)
      return True
    return False

  def has_flag(self, flag: str) -> bool:
    """
    Checks if the cell has a specific flag.

    Args:
      flag (str): The flag to check.

    Returns:
      bool: True if the flag is present, False otherwise.
    """
    return flag in self.__flags

  def list_flags(self) -> list[str]:
    """
    Lists the flags associated with the cell.

    Returns:
      list[str]: The list of flags.
    """
    return self.__flags
