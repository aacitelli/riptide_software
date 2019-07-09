#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from riptide_flexbe_states.move_to_buoys import MoveToBuoysState
from riptide_flexbe_states.align_static_buoy import AlignStaticBuoyState
from riptide_flexbe_states.align_moving_buoy import AlignMovingBouyState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 08 2019
@author: Parth Parekh
'''
class buoy_task_behaviorSM(Behavior):
	'''
	Does buoy task
	'''


	def __init__(self):
		super(buoy_task_behaviorSM, self).__init__()
		self.name = 'buoy_task_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:303 y:359
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:245 y:43
			OperatableStateMachine.add('Move to Buoys',
										MoveToBuoysState(),
										transitions={'success': 'touch static buoy and reset', 'failed': 'failed', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'failed': Autonomy.Off, 'command_error': Autonomy.Off})

			# x:55 y:165
			OperatableStateMachine.add('touch static buoy and reset',
										AlignStaticBuoyState(),
										transitions={'success': 'Touch spinning buoy', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'command_error': Autonomy.Off})

			# x:50 y:251
			OperatableStateMachine.add('Touch spinning buoy',
										AlignMovingBouyState(),
										transitions={'success': 'finished', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'command_error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
