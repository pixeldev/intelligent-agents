from typing import Optional

import flet

from src.agent.domain.agent import Agent
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


class PlayAgentFinishPositionSelectionViewUi(ViewUi):
  CELL_SIZE = 25
  SPACING = 5
  VISIBLE_COLUMNS = 26
  VISIBLE_ROWS = 26

  def __init__(self, environment_service: EnvironmentService, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_AGENT_FINISH_POSITION_SELECTION_SCREEN_IDENTIFIER)
    self.__environment_service: EnvironmentService = environment_service
    self.__view_service: ViewUiService = view_service
    self.grid_view: Optional[flet.Column] = None
    self.selected_position_text: Optional[flet.Text] = None
    self.last_selected_position_control: Optional[flet.Control] = None
    self.start_row: int = 0
    self.start_col: int = 0
    self.selected_position_row: int = 0
    self.selected_position_col: int = 0

  def select_position(self, event: flet.ControlEvent, row: int, col: int):
    self.selected_position_text.value = f'Posición seleccionada: ({row}, {col})'
    self.selected_position_text.update()
    self.set_selected_position_row(event.control, row, col)
    event.control.update()

  def set_selected_position_row(self, control: flet.Control, row: int, col: int):
    if self.last_selected_position_control is not None:
      self.last_selected_position_control.border = None
      self.last_selected_position_control.update()
    self.last_selected_position_control = control
    self.selected_position_row = row
    self.selected_position_col = col
    control.border = flet.border.all(color='#ff0000', width=4)

  def generate_top_row(self, start_col: int) -> flet.Row:
    return flet.Row(
      controls=[
                 flet.Container(width=self.CELL_SIZE, height=self.CELL_SIZE)  # Empty top-left corner
               ] + [
                 flet.Container(
                   width=self.CELL_SIZE,
                   height=self.CELL_SIZE,
                   content=flet.Text(str(col), style=UiConstants.SMALL_TEXT_STYLE, text_align=flet.TextAlign.CENTER)
                 ) for col in range(start_col, start_col + self.VISIBLE_COLUMNS)
               ],
      alignment=flet.MainAxisAlignment.CENTER,
      spacing=self.SPACING,
      run_spacing=self.SPACING
    )

  def generate_row_containers(self, row: int, start_col: int) -> list[flet.Container]:
    row_containers = [
      flet.Container(
        width=self.CELL_SIZE,
        height=self.CELL_SIZE,
        content=flet.Text(str(row), style=UiConstants.SMALL_TEXT_STYLE, text_align=flet.TextAlign.CENTER)
      )
    ]
    for col in range(start_col, start_col + self.VISIBLE_COLUMNS):
      cell: Optional[Cell] = self.__environment_service.get_environment().get_cell(row, col)
      if cell is None:
        continue
      cell_control: flet.Container = flet.Container(
        width=self.CELL_SIZE,
        height=self.CELL_SIZE,
        bgcolor=cell.get_terrain().get_color(),
        on_click=lambda event, selected_row=row, selected_col=col: self.select_position(event, selected_row, selected_col)
      )
      if row == self.selected_position_row and col == self.selected_position_col:
        self.set_selected_position_row(cell_control, row, col)
      row_containers.append(cell_control)
    return row_containers

  def generate_visible_cells(self, start_row: int, start_col: int) -> list[flet.Row]:
    grid_items: list[flet.Row] = []
    self.last_selected_position_control = None

    # Add the top row with numbers starting from start_col
    grid_items.append(self.generate_top_row(start_col))

    for row in range(start_row, start_row + self.VISIBLE_ROWS):
      row_containers = self.generate_row_containers(row, start_col)
      grid_items.append(
        flet.Row(
          controls=row_containers,
          alignment=flet.MainAxisAlignment.CENTER,
          spacing=self.SPACING,
          run_spacing=self.SPACING
        )
      )
    return grid_items

  def create_navigation_buttons(self) -> flet.Row:
    up_button = flet.ElevatedButton('⬆', style=UiConstants.BUTTON_STYLE, on_click=self.on_up_click)
    down_button = flet.ElevatedButton('⬇', style=UiConstants.BUTTON_STYLE, on_click=self.on_down_click)
    left_button = flet.ElevatedButton('⬅', style=UiConstants.BUTTON_STYLE, on_click=self.on_left_click)
    right_button = flet.ElevatedButton('➡', style=UiConstants.BUTTON_STYLE, on_click=self.on_right_click)

    return flet.Row(
      controls=[
        left_button,
        flet.Column(controls=[up_button, down_button]),
        right_button
      ],
      alignment=flet.MainAxisAlignment.CENTER
    )

  def create_control(self) -> list[flet.Control]:
    if self.__environment_service.get_environment() is None:
      return [
        flet.Text('No se ha seleccionado un mapa', style=UiConstants.TITLE_TEXT_STYLE)
      ]

    # Inicializar las celdas visibles
    grid_items: list[flet.Row] = self.generate_visible_cells(self.start_row, self.start_col)
    self.grid_view = flet.Column(
      controls=grid_items,
      spacing=self.SPACING,
      run_spacing=self.SPACING
    )

    navigation_controls = self.create_navigation_buttons()

    self.selected_position_text = flet.Text('Posición seleccionada: (0, 0)', text_align=flet.TextAlign.CENTER, style=UiConstants.NORMAL_TEXT_STYLE)

    left_section = flet.Column(
      controls=[
        self.grid_view,
        navigation_controls
      ],
      alignment=flet.MainAxisAlignment.CENTER,
      horizontal_alignment=flet.CrossAxisAlignment.CENTER
    )

    right_section = flet.Column(
      controls=[
        flet.Column(
          controls=[
            flet.Text('Meta del Agente', text_align=flet.TextAlign.CENTER, style=UiConstants.TITLE_TEXT_STYLE),
            flet.Text(
              'Haz click en una celda para seleccionar la posición final del agente',
              style=UiConstants.NORMAL_TEXT_STYLE,
              text_align=flet.TextAlign.CENTER,
              max_lines=3,  # Número máximo de líneas antes de hacer wrap
              no_wrap=False  # Hacer wrap del texto
            ),
            self.selected_position_text,
            flet.ElevatedButton('Siguiente', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.on_next_click(e))
          ],
          width=700,
          alignment=flet.MainAxisAlignment.CENTER,
          horizontal_alignment=flet.CrossAxisAlignment.CENTER
        )
      ],
      width=800,
      alignment=flet.MainAxisAlignment.CENTER,
      horizontal_alignment=flet.CrossAxisAlignment.CENTER
    )

    return [
      flet.Row(
        controls=[left_section, right_section],
        alignment=flet.MainAxisAlignment.CENTER,
        vertical_alignment=flet.CrossAxisAlignment.CENTER
      )
    ]

  def on_next_click(self, e: flet.ControlEvent):
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is None:
      return
    selected_agent: Optional[Agent] = environment.get_selected_agent()
    if selected_agent is None:
      return
    selected_agent.set_finish_position(self.selected_position_row, self.selected_position_col)
    self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_SCREEN_IDENTIFIER)

  def update_grid_view(self):
    new_grid_items = self.generate_visible_cells(self.start_row, self.start_col)
    self.grid_view.controls = new_grid_items
    self.grid_view.update()

  def on_up_click(self, e):
    if self.start_row > 0:
      self.start_row -= 1
      self.update_grid_view()

  def on_down_click(self, e):
    if self.start_row + self.VISIBLE_ROWS < self.__environment_service.get_environment().get_rows():
      self.start_row += 1
      self.update_grid_view()

  def on_left_click(self, e):
    if self.start_col > 0:
      self.start_col -= 1
      self.update_grid_view()

  def on_right_click(self, e):
    if self.start_col + self.VISIBLE_COLUMNS < self.__environment_service.get_environment().get_columns():
      self.start_col += 1
      self.update_grid_view()
