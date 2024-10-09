class Position:
  """
  Represents a position in a 2D space.

  Attributes:
    __x (int): The x-coordinate of the position.
    __y (int): The y-coordinate of the position.
  """

  def __init__(self, x: int, y: int):
    """
    Initializes a new Position instance.

    Args:
      x (int): The x-coordinate.
      y (int): The y-coordinate.
    """
    self.__x = x
    self.__y = y

  def get_x(self) -> int:
    """
    Gets the x-coordinate of the position.

    Returns:
      int: The x-coordinate.
    """
    return self.__x

  def get_y(self) -> int:
    """
    Gets the y-coordinate of the position.

    Returns:
      int: The y-coordinate.
    """
    return self.__y

  def __eq__(self, other: 'Position') -> bool:
    """
    Checks if this position is equal to another position.

    Args:
      other (Position): The other position to compare.

    Returns:
      bool: True if the positions are equal, False otherwise.
    """
    return self.__x == other.__x and self.__y == other.__y

  def __hash__(self) -> int:
    """
    Returns the hash value of the position.

    Returns:
      int: The hash value.
    """
    return hash((self.__x, self.__y))

  def __str__(self) -> str:
    """
    Returns the string representation of the position.

    Returns:
      str: The string representation.
    """
    return f'({self.__x}, {self.__y})'

  def __repr__(self) -> str:
    """
    Returns the official string representation of the position.

    Returns:
      str: The official string representation.
    """
    return f'Position({self.__x}, {self.__y})'

  def __add__(self, other: 'Position') -> 'Position':
    """
    Adds two positions.

    Args:
      other (Position): The other position to add.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x + other.__x, self.__y + other.__y)

  def __sub__(self, other: 'Position') -> 'Position':
    """
    Subtracts one position from another.

    Args:
      other (Position): The other position to subtract.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x - other.__x, self.__y - other.__y)

  def __mul__(self, other: 'Position') -> 'Position':
    """
    Multiplies two positions.

    Args:
      other (Position): The other position to multiply.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x * other.__x, self.__y * other.__y)

  def __truediv__(self, other: 'Position') -> 'Position':
    """
    Divides one position by another.

    Args:
      other (Position): The other position to divide by.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x // other.__x, self.__y // other.__y)

  def __floordiv__(self, other: 'Position') -> 'Position':
    """
    Floor divides one position by another.

    Args:
      other (Position): The other position to floor divide by.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x // other.__x, self.__y // other.__y)

  def __mod__(self, other: 'Position') -> 'Position':
    """
    Calculates the modulus of one position by another.

    Args:
      other (Position): The other position to mod by.

    Returns:
      Position: The resulting position.
    """
    return Position(self.__x % other.__x, self.__y % other.__y)

  def __lt__(self, other: 'Position') -> bool:
    """
    Checks if this position is less than another position.

    Args:
      other (Position): The other position to compare.

    Returns:
      bool: True if this position is less than the other, False otherwise.
    """
    return self.__x < other.__x or (self.__x == other.__x and self.__y < other.__y)

  def __le__(self, other: 'Position') -> bool:
    """
    Checks if this position is less than or equal to another position.

    Args:
      other (Position): The other position to compare.

    Returns:
      bool: True if this position is less than or equal to the other, False otherwise.
    """
    return self.__x <= other.__x or (self.__x == other.__x and self.__y <= other.__y)

  def __gt__(self, other: 'Position') -> bool:
    """
    Checks if this position is greater than another position.

    Args:
      other (Position): The other position to compare.

    Returns:
      bool: True if this position is greater than the other, False otherwise.
    """
    return self.__x > other.__x or (self.__x == other.__x and self.__y > other.__y)

  def __ge__(self, other: 'Position') -> bool:
    """
    Checks if this position is greater than or equal to another position.

    Args:
      other (Position): The other position to compare.

    Returns:
      bool: True if this position is greater than or equal to the other, False otherwise.
    """
    return self.__x >= other.__x or (self.__x == other.__x and self.__y >= other.__y)

  def __neg__(self) -> 'Position':
    """
    Negates the position.

    Returns:
      Position: The negated position.
    """
    return Position(-self.__x, -self.__y)

  def __abs__(self) -> 'Position':
    """
    Returns the absolute value of the position.

    Returns:
      Position: The position with absolute values.
    """
    return Position(abs(self.__x), abs(self.__y))
