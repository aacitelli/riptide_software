#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from riptide_flexbe_states.move_to_vamp_pickup import MoveToVampPickupState
from riptide_flexbe_states.align_vamp_pickup import AlignVampPickupState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 08 2019
@author: Parth
'''
class pickup_vamp_behaviorSM(Behavior):
	'''
	Pick up vamp and surface
	'''


	def __init__(self):
		super(pickup_vamp_behaviorSM, self).__init__()
		self.name = 'pickup_vamp_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:57 y:451, x:451 y:433
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Move to vamp pickup',
										MoveToVampPickupState(),
										transitions={'success': 'Align and Rise', 'failed': 'failed', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'failed': Autonomy.Off, 'command_error': Autonomy.Off})

			# x:92 y:265
			OperatableStateMachine.add('Align and Rise',
										AlignVampPickupState(),
										transitions={'success': 'finished', 'command_error': 'finished'},
										autonomy={'success': Autonomy.Off, 'command_error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
