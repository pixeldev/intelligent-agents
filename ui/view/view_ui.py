from abc import ABC, abstractmethod

import flet


class ViewUi(ABC):
  def __init__(self, identifier: str):
    self.__identifier: str = identifier

  def get_identifier(self) -> str:
    return self.__identifier

  @abstractmethod
  def create_control(self) -> list[flet.Control]:
    pass

  def render(self, page: flet.Page) -> None:
    page.controls.clear()
    for control in self.create_control():
      page.add(control)
    page.update()
