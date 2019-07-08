#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from riptide_flexbe_states.move_to_garlic_drop import MoveToGarlicDropState
from riptide_flexbe_states.align_garlic_drop import AlignGarlicDropState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 08 2019
@author: Parth
'''
class garlic_drop_behaviorSM(Behavior):
	'''
	Drops the garlic
	'''


	def __init__(self):
		super(garlic_drop_behaviorSM, self).__init__()
		self.name = 'garlic_drop_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:489 y:346
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:128 y:71
			OperatableStateMachine.add('Move to Garlic Bin',
										MoveToGarlicDropState(),
										transitions={'success': 'Align to Garlic Bin', 'failed': 'failed', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'failed': Autonomy.Off, 'command_error': Autonomy.Off})

			# x:109 y:217
			OperatableStateMachine.add('Align to Garlic Bin',
										AlignGarlicDropState(),
										transitions={'success': 'finished', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'command_error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
