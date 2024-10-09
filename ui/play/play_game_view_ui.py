from typing import Optional

import flet
from rich.cells import cell_len

from src.agent.domain.agent import Agent
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants
from ui.view.view_ui_repository import ViewUiService


# noinspection DuplicatedCode
class PlayGameViewUi(ViewUi):
  CELL_SIZE = 25
  SPACING = 5
  VISIBLE_COLUMNS = 26
  VISIBLE_ROWS = 26

  def __init__(self, environment_service: EnvironmentService, view_service: ViewUiService):
    super().__init__(ViewUiConstants.PLAY_GAME_SCREEN_IDENTIFIER)
    self.__environment_service: EnvironmentService = environment_service
    self.__view_service: ViewUiService = view_service
    self.grid_view: Optional[flet.Column] = None
    self.cell_terrain_control: Optional[flet.Text] = None
    self.cell_position_control: Optional[flet.Text] = None
    self.cell_cost_control: Optional[flet.Text] = None
    self.cell_flags_control: Optional[flet.Text] = None
    self.last_selected_cell_control: Optional[flet.Control] = None
    self.start_row: int = 0
    self.start_col: int = 0
    self.selected_cell_row: int = 0
    self.selected_cell_col: int = 0

  def update_cell_information(self, row: int, col: int):
    environment: Optional[Environment] = self.__environment_service.get_environment()
    if environment is None:
      return

    self.cell_position_control.value = f'Celda seleccionada: ({row}, {col})'

    cell: Optional[Cell] = environment.get_cell(row, col)
    if cell is None:
      return

    self.cell_terrain_control.value = f'Terreno: {cell.get_terrain().get_display_name()} ({cell.get_terrain().get_code()})'

    selected_agent: Optional[Agent] = environment.get_selected_agent()
    if selected_agent is None:
      return

    movement_cost: int = cell.get_movement_cost_for(selected_agent.get_name())
    self.cell_cost_control.value = f'Costo: {movement_cost if movement_cost is not None else "No puede pasar."}'

    flags: list[str] = selected_agent.list_flags(row, col)
    flags_len: int = len(flags)
    if flags_len == 0:
      self.cell_flags_control.value = 'No hay marcas'
    else:
      self.cell_flags_control.value = f'Marcas: {', '.join(flags)}'

  def on_click_cell(self, event: flet.ControlEvent, row: int, col: int):
    self.update_cell_information(row, col)
    self.cell_position_control.update()
    self.cell_terrain_control.update()
    self.cell_cost_control.update()
    self.cell_flags_control.update()
    self.set_selected_cell(event.control, row, col)
    event.control.update()

  def set_selected_cell(self, control: flet.Control, row: int, col: int):
    if self.last_selected_cell_control is not None:
      self.last_selected_cell_control.border = None
      self.last_selected_cell_control.update()
    self.last_selected_cell_control = control
    self.selected_cell_row = row
    self.selected_cell_col = col
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
    row_containers: list[flet.Container] = [
      flet.Container(
        width=self.CELL_SIZE,
        height=self.CELL_SIZE,
        content=flet.Text(str(row), style=UiConstants.SMALL_TEXT_STYLE, text_align=flet.TextAlign.CENTER)
      )
    ]

    selected_agent: Optional[Agent] = self.__environment_service.get_environment().get_selected_agent()
    if selected_agent is None:
      return row_containers

    for col in range(start_col, start_col + self.VISIBLE_COLUMNS):
      cell: Optional[Cell] = self.__environment_service.get_environment().get_cell(row, col)
      if cell is None:
        continue
      if not selected_agent.is_known(row, col):
        row_containers.append(
          flet.Container(
            width=self.CELL_SIZE,
            height=self.CELL_SIZE,
            bgcolor='#000000'
          )
        )
        continue
      cell_control: flet.Container = flet.Container(
        width=self.CELL_SIZE,
        height=self.CELL_SIZE,
        bgcolor=cell.get_terrain().get_color(),
        on_click=lambda event, selected_row=row, selected_col=col: self.on_click_cell(event, selected_row, selected_col)
      )
      if row == self.selected_cell_row and col == self.selected_cell_col:
        self.set_selected_cell(cell_control, row, col)
      if selected_agent.is_in_position(row, col):
        cell_control.border = flet.border.all(color='#00ff00', width=4)
        self.update_cell_information(row, col)
      row_containers.append(cell_control)
    return row_containers

  def generate_visible_cells(self, start_row: int, start_col: int) -> list[flet.Row]:
    grid_items: list[flet.Row] = []
    self.last_selected_cell_control = None

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
    environment: Environment = self.__environment_service.get_environment()
    if environment is None:
      return [
        flet.Text('No se ha seleccionado un mapa', style=UiConstants.TITLE_TEXT_STYLE),
        flet.ElevatedButton('Regresar', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.__view_service.navigate_to(ViewUiConstants.PLAY_MAP_SELECTION_SCREEN_IDENTIFIER))
      ]

    self.cell_position_control = flet.Text(text_align=flet.TextAlign.CENTER, style=UiConstants.NORMAL_TEXT_STYLE)
    self.cell_terrain_control = flet.Text(text_align=flet.TextAlign.CENTER, style=UiConstants.NORMAL_TEXT_STYLE)
    self.cell_cost_control = flet.Text(text_align=flet.TextAlign.CENTER, style=UiConstants.NORMAL_TEXT_STYLE)
    self.cell_flags_control = flet.Text(text_align=flet.TextAlign.CENTER, style=UiConstants.NORMAL_TEXT_STYLE)

    selected_agent: Optional[Agent] = environment.get_selected_agent()
    self.start_row = selected_agent.get_x() if selected_agent.get_x() - self.VISIBLE_ROWS >= 0 else 0
    self.start_col = selected_agent.get_y() if selected_agent.get_y() - self.VISIBLE_COLUMNS >= 0 else 0

    # Inicializar las celdas visibles
    grid_items: list[flet.Row] = self.generate_visible_cells(self.start_row, self.start_col)
    self.grid_view = flet.Column(
      controls=grid_items,
      spacing=self.SPACING,
      run_spacing=self.SPACING
    )

    navigation_controls = self.create_navigation_buttons()

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
            flet.Column(
              controls=[
                flet.Text('Celda', text_align=flet.TextAlign.CENTER, style=UiConstants.TITLE_TEXT_STYLE),
                self.cell_position_control,
                self.cell_terrain_control,
                self.cell_cost_control,
                self.cell_flags_control
              ],
              alignment=flet.MainAxisAlignment.CENTER,
              horizontal_alignment=flet.CrossAxisAlignment.CENTER
            ),
            flet.Column(
              controls=[
                flet.Text('Agente', text_align=flet.TextAlign.CENTER, style=UiConstants.TITLE_TEXT_STYLE),
                flet.Text(f'Posición: ({selected_agent.get_x()}, {selected_agent.get_y()})', text_align=flet.TextAlign.LEFT, style=UiConstants.NORMAL_TEXT_STYLE),
                flet.Text(f'Movimientos: {selected_agent.get_steps()}', text_align=flet.TextAlign.LEFT, style=UiConstants.NORMAL_TEXT_STYLE),
                flet.Text(f'Costo acumulado: {selected_agent.get_accumulated_movement_cost()}', text_align=flet.TextAlign.LEFT, style=UiConstants.NORMAL_TEXT_STYLE)
              ],
              alignment=flet.MainAxisAlignment.CENTER,
              horizontal_alignment=flet.CrossAxisAlignment.CENTER
            ),
            flet.Column(
              controls=[
                flet.ElevatedButton('Sensores', style=UiConstants.BUTTON_STYLE, on_click=self.on_click_sensors),
                flet.ElevatedButton('Acciones', style=UiConstants.BUTTON_STYLE, on_click=self.on_click_actions),
                flet.ElevatedButton('Salir', style=UiConstants.BUTTON_STYLE, on_click=lambda e: self.__view_service.navigate_to(ViewUiConstants.MAIN_SCREEN_IDENTIFIER))
              ],
              alignment=flet.MainAxisAlignment.CENTER,
              horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
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

  def on_click_sensors(self, e: flet.ControlEvent):
    self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_SENSORS_SCREEN_IDENTIFIER)

  def on_click_actions(self, e: flet.ControlEvent):
    self.__view_service.navigate_to(ViewUiConstants.PLAY_GAME_ACTIONS_SCREEN_IDENTIFIER)

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
