import flet


class UiConstants:
  TITLE_TEXT_STYLE: flet.TextStyle = flet.TextStyle(font_family="Comic Neue", size=96)
  NORMAL_TEXT_STYLE: flet.TextStyle = flet.TextStyle(font_family="Comic Neue", size=36)
  MEDIUM_TEXT_STYLE: flet.TextStyle = flet.TextStyle(font_family="Comic Neue", size=24)
  SMALL_TEXT_STYLE: flet.TextStyle = flet.TextStyle(font_family="Comic Neue", size=12)
  BUTTON_STYLE: flet.ButtonStyle = flet.ButtonStyle(text_style=NORMAL_TEXT_STYLE, shape=flet.RoundedRectangleBorder(radius=25), padding=25)

  EMPTY_CELL_COLOR: str = "#FFFFFF"

