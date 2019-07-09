#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from riptide_flexbe_behaviors.startup_behavior_sm import startup_behaviorSM
from riptide_flexbe_behaviors.gate_task_sm import gate_taskSM
from riptide_flexbe_behaviors.slay_vamp_behavior_sm import slay_vamp_behaviorSM
from riptide_flexbe_behaviors.garlic_drop_behavior_sm import garlic_drop_behaviorSM
from riptide_flexbe_behaviors.buoy_task_behavior_sm import buoy_task_behaviorSM
from riptide_flexbe_behaviors.pickup_vamp_behavior_sm import pickup_vamp_behaviorSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 08 2019
@author: Parth Parekh
'''
class Be_AutonomousSM(Behavior):
	'''
	Be autonomous
	'''


	def __init__(self):
		super(Be_AutonomousSM, self).__init__()
		self.name = 'Be_Autonomous'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(startup_behaviorSM, 'startup_behavior')
		self.add_behavior(gate_taskSM, 'gate_task')
		self.add_behavior(slay_vamp_behaviorSM, 'slay_vamp_behavior')
		self.add_behavior(garlic_drop_behaviorSM, 'garlic_drop_behavior')
		self.add_behavior(buoy_task_behaviorSM, 'buoy_task_behavior')
		self.add_behavior(pickup_vamp_behaviorSM, 'pickup_vamp_behavior')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:21 y:644, x:466 y:569
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('startup_behavior',
										self.use_behavior(startup_behaviorSM, 'startup_behavior'),
										transitions={'finished': 'gate_task', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:30 y:138
			OperatableStateMachine.add('gate_task',
										self.use_behavior(gate_taskSM, 'gate_task'),
										transitions={'finished': 'slay_vamp_behavior', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:30 y:236
			OperatableStateMachine.add('slay_vamp_behavior',
										self.use_behavior(slay_vamp_behaviorSM, 'slay_vamp_behavior'),
										transitions={'finished': 'buoy_task_behavior', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:31 y:440
			OperatableStateMachine.add('garlic_drop_behavior',
										self.use_behavior(garlic_drop_behaviorSM, 'garlic_drop_behavior'),
										transitions={'finished': 'pickup_vamp_behavior', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:30 y:334
			OperatableStateMachine.add('buoy_task_behavior',
										self.use_behavior(buoy_task_behaviorSM, 'buoy_task_behavior'),
										transitions={'finished': 'garlic_drop_behavior', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:136 y:538
			OperatableStateMachine.add('pickup_vamp_behavior',
										self.use_behavior(pickup_vamp_behaviorSM, 'pickup_vamp_behavior'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
