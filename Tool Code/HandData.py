import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

# with open('HandData.csv', mode = 'w') as hand_data:
# 	data_writer = csv.writer(hand_data, delimiter = '')

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

	def on_init(self, controller):
		print("Initialized")
		controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD) #Currently optimized for HMD display

	def on_connect(self, controller):
		print("Motion Sensor Connected")

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);#have to use semicolon here
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		print ("Motion Sensor Disconnected")

	def on_exit(self, controller):
		print ("Exited")

	def on_frame(self, controller):
		frame = controller.frame()

		###########
		#Frame Data
		fid = frame.id
		timestamp = frame.timestamp
		num_hands = len(frame.hands)
		num_fingers = len(frame.fingers)
		num_tools = len(frame.tools)
		num_gestures = len(frame.gestures())

		# print "Frame ID:  " + str(fid) \
		# 	+ " Timestamp: " + str(timestamp) \
		# 	+ " # of Hands: " + str(num_hands) \
		# 	+ " # of Fingers: " + str(num_fingers) \
		# 	+ " # of Tools: " + str(num_tools) \
		# 	+ " # of Gestures: " + str(num_gestures)

		for hand in frame.hands:
			handType = "\nLeft Hand" if hand.is_left else "\nRight Hand"
			hid = hand.id
			palm_pos = hand.palm_position

			print handType + " Hand ID: " + str(hid) + ", Palm Position: " + str(palm_pos) 
			#x is leftright, y is up down, z is depth

			#normal is vector normal to palm
			normal = hand.palm_normal
			direction = hand.direction

			########################
			#Pitch Roll and Yaw Data
			pitch = direction.pitch * Leap.RAD_TO_DEG
			roll = normal.roll * Leap.RAD_TO_DEG
			yaw = direction.yaw * Leap.RAD_TO_DEG
			# print "Pitch: " + str(pitch) + ", Roll: " + str(roll) + ", Yaw: " + str(yaw)

			#########
			#arm data
			arm = hand.arm
			arm_dir = arm.direction
			wrist_pos = arm.wrist_position
			elbow_pos = arm.elbow_position
			# print "Arm Direction: " + str(arm_dir) + ", Wrist Position: " + str(wrist_pos) + ", Elbow Position: " + str(elbow_pos)

			############
			#finger data
			for finger in hand.fingers:
				finger_name = self.finger_names[finger.type]
				finger_id = finger.id
				finger_length = finger.length
				finger_width = finger.width
				print finger_name + " finger, ID: " + str(finger_id) + ", Finger Length(mm): " + str(finger_length) + ", Finger Width(mm): " + str(finger_width)

				##########
				#bone data
				for b in range(0, 4):
					bone = finger.bone(b)
					bone_name = self.bone_names[bone.type]
					start = bone.prev_joint #returns vector where bone started (closest to wrist)
					end = bone.next_joint #returns vector where bone ends (and next bone starts)
					bone_dir = bone.direction
					print "Bone: " + bone_name + ", Start: " + str(start) + ", End: " + str(end) + ", Direction: " + str(bone_dir)


def main():
	start = time.time()
	listener = LeapMotionListener()
	controller = Leap.Controller()

	while time.time() - start < 5: #5 second timer for data collection
		controller.add_listener(listener)
	controller.remove_listener(listener)
	# try:
	# 	# sys.stdin.readline()
	# except KeyboardInterrupt:
	# 	pass
	# finally:
	# 	controller.remove_listener(listener)

if __name__ == '__main__':
	main()
