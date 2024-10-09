class Map:
  """Entity that represents a terrain map.

  Attributes:
    __grid (list[list[int]]): 2D list representing the terrain grid.
    __rows (int): Number of rows in the map.
    __columns (int): Number of columns in the map
  """

  def __init__(self, grid: list[list[int]], rows: int, columns: int):
    """
    Initializes a Map instance.

    Args:
      rows (int): Number of rows in the map.
      columns (int): Number of columns in the map.
      grid (list[list[int]]): 2D list representing the terrain grid.
    """
    self.__grid = grid
    self.__rows = rows
    self.__columns = columns

  def get_rows(self) -> int:
    """
    Returns the number of rows in the map.

    Returns:
      int: The number of rows in the map.
    """
    return self.__rows

  def get_columns(self) -> int:
    """
    Returns the number of columns in the map.

    Returns:
      int: The number of columns in the map.
    """
    return self.__columns

  def get_cell(self, x: int, y: int) -> int:
    """
    Retrieves the value of a cell in the grid.

    Args:
      x (int): The row index of the cell.
      y (int): The column index of the cell.

    Returns:
      int: The value of the cell at the specified coordinates.
    """
    return self.__grid[x][y]

  def print(self):
    """
    Prints the grid to the console in a grid format.
    """
    print('-= Map =-')
    print(f'Rows: {self.__rows}')
    print(f'Columns: {self.__columns}')

    # Print top border
    print('┌' + '┬'.join(['─' * 3] * self.__columns) + '┐')

    for row in range(self.__rows):
      # Print row with values
      print('│' + '│'.join([f' {str(cell)} ' for cell in self.__grid[row]]) + '│')
      # Print row separator
      if row != self.__rows - 1:
        print('├' + '┼'.join(['─' * 3] * self.__columns) + '┤')

    # Replace the last row separator with the bottom border
    print('└' + '┴'.join(['─' * 3] * self.__columns) + '┘')
