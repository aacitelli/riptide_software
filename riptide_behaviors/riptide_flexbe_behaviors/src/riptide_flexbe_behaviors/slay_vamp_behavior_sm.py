#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from riptide_flexbe_states.move_to_slay_state import MoveToSlayState
from riptide_flexbe_states.align_to_slay_state import AlignSlayState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 08 2019
@author: Parth Parekh
'''
class slay_vamp_behaviorSM(Behavior):
	'''
	Slays the Vampire... What else you want from it?
	'''


	def __init__(self):
		super(slay_vamp_behaviorSM, self).__init__()
		self.name = 'slay_vamp_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:218 y:42
			OperatableStateMachine.add('Move to Slay',
										MoveToSlayState(),
										transitions={'success': 'Align To Slay', 'failed': 'failed', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'failed': Autonomy.Off, 'command_error': Autonomy.Off})

			# x:19 y:198
			OperatableStateMachine.add('Align To Slay',
										AlignSlayState(),
										transitions={'success': 'finished', 'command_error': 'failed'},
										autonomy={'success': Autonomy.Off, 'command_error': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
