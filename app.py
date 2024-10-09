import os

import flet

from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.action.move_down_action import MoveDownAction
from src.agent.domain.action.move_left_action import MoveLeftAction
from src.agent.domain.action.move_right_action import MoveRightAction
from src.agent.domain.action.move_up_action import MoveUpAction
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.down_directional_sensor import DownDirectionalSensor
from src.agent.domain.sensor.left_directional_sensor import LeftDirectionalSensor
from src.agent.domain.sensor.merged_sensor import MergedSensor
from src.agent.domain.sensor.right_directional_sensor import RightDirectionalSensor
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor_repository import SensorRepository
from src.agent.domain.sensor.up_directional_sensor import UpDirectionalSensor
from src.environment.application.environment_agent_service import EnvironmentAgentService, ExecuteActionResult, ResultCode, ExecuteSensorResult
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map_repository import MapRepository
from ui.app_ui import AppUi

if __name__ == '__main__':
  project_root = os.path.dirname(os.path.abspath(__file__))

  terrain_repository: TerrainRepository = TerrainRepository(f'{project_root}/resources/terrain')
  map_repository: MapRepository = MapRepository(f'{project_root}/resources/map')
  environment_service: EnvironmentService = EnvironmentService(map_repository, terrain_repository)

  action_repository: ActionRepository = ActionRepository()
  action_repository.add_actions(MoveUpAction(), MoveDownAction(), MoveLeftAction(), MoveRightAction())

  sensor_repository: SensorRepository = SensorRepository()
  up_directional_sensor: UpDirectionalSensor = UpDirectionalSensor()
  down_directional_sensor: DownDirectionalSensor = DownDirectionalSensor()
  left_directional_sensor: LeftDirectionalSensor = LeftDirectionalSensor()
  right_directional_sensor: RightDirectionalSensor = RightDirectionalSensor()

  sensor_repository.add_sensors(
    up_directional_sensor,
    down_directional_sensor,
    left_directional_sensor,
    right_directional_sensor,
    MergedSensor('up_down', [up_directional_sensor, down_directional_sensor]),
    MergedSensor('left_right', [left_directional_sensor, right_directional_sensor]),
    MergedSensor('every_direction', [up_directional_sensor, down_directional_sensor, left_directional_sensor, right_directional_sensor])
  )

  environment_agent_service: EnvironmentAgentService = EnvironmentAgentService(action_repository, sensor_repository)

  # environment.add_agent(human_agent)
  #
  # environment.print_discovered_map()
  #
  # execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  # print('Action result:', execute_action_result.get_action_result())
  #
  # execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, DownDirectionalSensor.IDENTIFIER)
  # print('Sensor result:', execute_sensor_result.get_sensor_result())
  #
  # environment.print_discovered_map()
  #
  # execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  # print('Action result:', execute_action_result.get_action_result())
  #
  # print('--= Agent information =--')
  # print(f'Position: ({human_agent.get_x()}, {human_agent.get_y()})')
  # print(f'Direction: {human_agent.get_direction()}')
  # print(f'Steps: {human_agent.get_steps()}')
  # print(f'Accumulated Movement Cost: {human_agent.get_accumulated_movement_cost()}')
  # print('--= ----- =--')
  #
  # environment.print_discovered_map()
  #
  # execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, 'every_direction')
  # print('Sensor result:', execute_sensor_result.get_sensor_result())
  #
  # environment.print_discovered_map()
  #
  # execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveRightAction.IDENTIFIER)
  # print('Action result:', execute_action_result.get_action_result())
  #
  # print('--= Agent information =--')
  # print(f'Position: ({human_agent.get_x()}, {human_agent.get_y()})')
  # print(f'Direction: {human_agent.get_direction()}')
  # print(f'Steps: {human_agent.get_steps()}')
  # print(f'Accumulated Movement Cost: {human_agent.get_accumulated_movement_cost()}')
  # print('--= ----- =--')
  #
  # environment.print_discovered_map()
  #
  # execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, 'every_direction')
  # print('Sensor result:', execute_sensor_result.get_sensor_result())
  #
  # environment.print_discovered_map()

  app_ui: AppUi = AppUi(environment_agent_service, environment_service, map_repository, terrain_repository)

  flet.app(target=app_ui.start)
