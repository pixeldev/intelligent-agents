from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.action.move_down_action import MoveDownAction
from src.agent.domain.action.move_left_action import MoveLeftAction
from src.agent.domain.action.move_right_action import MoveRightAction
from src.agent.domain.action.move_up_action import MoveUpAction
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.down_directional_sensor import DownDirectionalSensor
from src.agent.domain.sensor.left_directional_sensor import LeftDirectionalSensor
from src.agent.domain.sensor.right_directional_sensor import RightDirectionalSensor
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.up_directional_sensor import UpDirectionalSensor


class DefaultAgents:
  DEFAULT_ACTIONS: dict[str, ActionConfiguration] = {
    MoveUpAction.IDENTIFIER: ActionConfiguration('Desplaza el agente una posición hacía arriba.', 'Mover hacía arriba', MoveUpAction.IDENTIFIER, {'steps': 1}),
    MoveDownAction.IDENTIFIER: ActionConfiguration('Desplaza el agente una posición hacía abajo.', 'Mover hacía abajo', MoveDownAction.IDENTIFIER, {'steps': 1}),
    MoveLeftAction.IDENTIFIER: ActionConfiguration('Desplaza el agente una posición hacía la izquierda.', 'Mover hacía la izquierda', MoveLeftAction.IDENTIFIER, {'steps': 1}),
    MoveRightAction.IDENTIFIER: ActionConfiguration('Desplaza el agente una posición hacía la derecha.', 'Mover hacía la derecha', MoveRightAction.IDENTIFIER, {'steps': 1})
  }

  DEFAULT_SENSORS: dict[str, SensorConfiguration] = {
    UpDirectionalSensor.IDENTIFIER: SensorConfiguration('Sensar las celdas arriba del agente.', 'Hacía arriba', UpDirectionalSensor.IDENTIFIER, False, 1),
    DownDirectionalSensor.IDENTIFIER: SensorConfiguration('Sensar las celdas debajo del agente.', 'Hacía abajo', DownDirectionalSensor.IDENTIFIER, False, 1),
    LeftDirectionalSensor.IDENTIFIER: SensorConfiguration('Sensar las celdas a la izquierda del agente.', 'Hacía la izquierda', LeftDirectionalSensor.IDENTIFIER, False, 1),
    RightDirectionalSensor.IDENTIFIER: SensorConfiguration('Sensar las celdas a la derecha del agente.', 'Hacía la derecha', RightDirectionalSensor.IDENTIFIER, False, 1),
    'up_down': SensorConfiguration('Sensar las celdas arriba y abajo del agente.', 'Arriba y Abajo', 'up_down', False, 1),
    'left_right': SensorConfiguration('Sensar las celdas de izquierda y derecha del agente.', 'Izquierda y Derecha', 'left_right', False, 1),
    'every_direction': SensorConfiguration('Sensar las celdas arriba, abajo, izquierda y derecha del agente.', 'Todas las direcciones', 'every_direction', True, 1)
  }

  @staticmethod
  def create_agent(name: str, columns: int, rows: int) -> Agent:
    return Agent(
      0,
      DefaultAgents.DEFAULT_ACTIONS,
      None,
      [[None for _ in range(rows)] for _ in range(columns)],
      name,
      DefaultAgents.DEFAULT_SENSORS,
      0,
      0,
      0)
