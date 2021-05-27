import bpy
import math
import bmesh


#Setting constraints of hand and resets rotation
bpy.ops.object.h_constraints()

view_layer = bpy.context.view_layer
context = bpy.context
#Mesh Objects
lh_mesh = bpy.data.objects['Hand.L']
rh_mesh = bpy.data.objects['Hand.R']
joystick = bpy.data.objects['Joystick']
bm_joy = bmesh.new()
bm_left = bmesh.new()
bm_right = bmesh.new()

#Grab Mesh Data
context.active_object.select_set(False)
view_layer.objects.active = lh_mesh
bm_left.from_mesh(context.object.data)
print('LH Mesh Volume = ' + str(bm_left.calc_volume()))
#bm_left.faces.ensure_lookup_table() #allows iteration of faces
#verts = bm_left.faces[-1].verts[:]
#print(verts)
#for v in bm_left.verts:
#    print(v.co)
#print(bm_left.verts.calc_edge_angle())

context.active_object.select_set(False)
view_layer.objects.active = rh_mesh
bm_right.from_mesh(context.object.data)

print('RH Mesh Volume = ' + str(bm_right.calc_volume()))
#so = context.active_object
#verts = so.data.vertices
#edges = so.data.edges
#faces = so.data.polygons

#Armature Objects
hand_left = bpy.data.objects['Hand_Left']
hand_right = bpy.data.objects['Hand_Right']




#Thumbs up pose
context.active_object.select_set(False)
view_layer.objects.active = hand_left
pbone = context.object.pose.bones['index control']
pbone.rotation_euler[0] = math.radians(-80)
pbone = context.object.pose.bones['Major control']
pbone.rotation_euler[0] = math.radians(-80)
pbone = context.object.pose.bones['Ring control']
pbone.rotation_euler[0] = math.radians(-80)
pbone = context.object.pose.bones['Pinky control']
pbone.rotation_euler[0] = math.radians(-80)
pbone = context.object.pose.bones['Bone.017']
pbone.rotation_euler[0] = math.radians(27.5)
pbone = context.object.pose.bones['Bone.016']
pbone.rotation_euler[0] = math.radians(1.93)
pbone.rotation_euler[1] = math.radians(-12.1)
pbone.rotation_euler[2] = math.radians(-7.06)
pbone = context.object.pose.bones['Bone.020']
pbone.rotation_euler[0] = math.radians(0)
pbone.rotation_euler[1] = math.radians(80.5)
pbone.rotation_euler[2] = math.radians(0)

#overlaying joystick on top of hand
context.active_object.select_set(False)
view_layer.objects.active = joystick
so = bpy.context.active_object
so.location = (0.84, -0.06, 0)



#for v in verts:
#    print(v.co)
step = 10 #10 degree increment

