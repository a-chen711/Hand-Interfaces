import bpy
import math
import bmesh
gesture = 0


def bmesh_copy_from_object(obj, transform=True, triangulate=True, apply_modifiers=False):
    """Returns a transformed, triangulated copy of the mesh"""

    assert obj.type == 'MESH'

    if apply_modifiers and obj.modifiers:
        import bpy
        depsgraph = bpy.context.evaluated_depsgraph_get()
        obj_eval = obj.evaluated_get(depsgraph)
        me = obj_eval.to_mesh()
        bm = bmesh.new()
        bm.from_mesh(me)
        obj_eval.to_mesh_clear()
    else:
        me = obj.data
        if obj.mode == 'EDIT':
            bm_orig = bmesh.from_edit_mesh(me)
            bm = bm_orig.copy()
        else:
            bm = bmesh.new()
            bm.from_mesh(me)

    # TODO. remove all customdata layers.
    # would save ram

    if transform:
        bm.transform(obj.matrix_world)

    if triangulate:
        bmesh.ops.triangulate(bm, faces=bm.faces)

    return bm
    
#Setting constraints of hand and resets rotation
#bpy.ops.object.h_constraints()

view_layer = bpy.context.view_layer
context = bpy.context
scene = context.scene


#Mesh Objects
lh_mesh = bpy.data.objects['Hand.L']
#rh_mesh = bpy.data.objects['Hand.R']
sphere = bpy.data.objects['Sphere']
bm_joy = bmesh.new()
bm_left = bmesh.new()
bm_right = bmesh.new()

#Grab Mesh Data
context.active_object.select_set(False)
view_layer.objects.active = lh_mesh
bm_left.from_mesh(context.object.data)
lh_volume = bm_left.calc_volume()-0.00622
print('LH Mesh Volume = ' + str(lh_volume))

#context.active_object.select_set(False)
#view_layer.objects.active = rh_mesh
#bm_right.from_mesh(context.object.data)

#print('RH Mesh Volume = ' + str(bm_right.calc_volume()))
#so = context.active_object
#verts = so.data.vertices
#edges = so.data.edges
#faces = so.data.polygons

#Armature Objects
hand_left = bpy.data.objects['Hand_Left']
#hand_right = bpy.data.objects['Hand_Right']
view_layer.objects.active = hand_left


#Thumbs up pose
if gesture == 0:
    context.active_object.select_set(False)
    view_layer.objects.active = hand_left
    pbone = context.object.pose.bones['index control']
    pbone.rotation_euler[0] = math.radians(0)
    pbone = context.object.pose.bones['Major control']
    pbone.rotation_euler[0] = math.radians(0)
    pbone = context.object.pose.bones['Ring control']
    pbone.rotation_euler[0] = math.radians(0)
    pbone = context.object.pose.bones['Pinky control']
    pbone.rotation_euler[0] = math.radians(0)
    pbone = context.object.pose.bones['Bone.017']
    pbone.rotation_euler[0] = math.radians(27.5)
    pbone = context.object.pose.bones['Bone.016']
    pbone.rotation_euler[0] = math.radians(1.93)
    pbone.rotation_euler[1] = math.radians(-12.1)
    pbone.rotation_euler[2] = math.radians(-7.06)
    pbone = context.object.pose.bones['Bone.020']
    pbone.rotation_euler[0] = math.radians(-20)
    pbone.rotation_euler[1] = math.radians(80)
    pbone.rotation_euler[2] = math.radians(0)
elif gesture == 1:
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
    pbone.rotation_euler[0] = math.radians(-20)
    pbone.rotation_euler[1] = math.radians(80)
    pbone.rotation_euler[2] = math.radians(0)

#normalizing volume of sphere to the volume of the hand
context.active_object.select_set(False)
sphere = scene.objects.get("Sphere")
joystick = scene.objects.get("Joystick")
test_object = joystick

view_layer.objects.active = test_object
so = bpy.context.active_object
m_sphere = bmesh_copy_from_object(test_object, apply_modifiers=True)
volume = m_sphere.calc_volume()
m_sphere.free()

scale_ratio = lh_volume/volume
scale_factor = scale_ratio ** (1/3)
print('Mesh (BEFORE) Volume = ' + str(volume))

test_object.select_set(True)
bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
m_sphere = bmesh_copy_from_object(test_object, apply_modifiers=True) #update the m_sphere
print('Mesh (AFTER SCALE) Volume = ' + str(m_sphere.calc_volume()))
so = bpy.context.active_object
if test_object == sphere:
    so.location = (0,-0.03,0)
so.rotation_euler[0] = math.radians(0)
so.rotation_euler[1] = math.radians(0)
#m_sphere.free()

#Apply intersect operator
bpy.ops.object.modifier_add(type = 'BOOLEAN')
context.object.modifiers["Boolean"].operation = 'INTERSECT'            
bpy.context.object.modifiers["Boolean"].object = lh_mesh


bone_num = ['index control', 'Major control', 'Ring control', 'Pinky control', 'Bone.017']
increment = -20
pose_max_vol = m_sphere.calc_volume()
rot_index = 0
finger_index = 0
angle = 0
#don't have to do every single combination since some are very similar so let's say 20 degree difference
##loop
for i in range(4):
    print('Computing ' + bone_num[i])
    for j in range(0, -100, increment):
        context.active_object.select_set(False)
        view_layer.objects.active = hand_left
        pbone = context.object.pose.bones[bone_num[i]]
        pbone.rotation_euler[0] = math.radians(j)
        rot_max_vol = 0
        #I will start all objects in the UP direction, so we don't need to check that twice
        #0 DOWN, 1 FORWARD, 2 BACKWARD, 3 RIGHT, 4 LEFT
        for x in range(5):
            m_volume = bmesh_copy_from_object(test_object, apply_modifiers=True) #update the m_sphere
            rot_curr_vol = m_volume.calc_volume()
            print('curr_volume = ' + str(rot_curr_vol))
            if rot_curr_vol > rot_max_vol: #check max volume
                rot_max_vol = rot_curr_vol
                rot_index = x
                finger_index = i
                angle = j
            view_layer.objects.active = test_object
            #rotate
            if x == 0:
                context.active_object.rotation_euler[0] = math.radians(180) #DOWN
            elif x == 1:
                context.active_object.rotation_euler[0] = math.radians(90) #FORWARD
            elif x == 2:
                context.active_object.rotation_euler[0] = math.radians(-90) #BACKWARDS
            elif x == 3:
                context.active_object.rotation_euler[1] = math.radians(-90) #RIGHT
            elif x == 4:
                context.active_object.rotation_euler[1] = math.radians(90) #LEFT 
        print('rot_max_vol = ' + str(rot_max_vol))                           
        if rot_max_vol > pose_max_vol:
            pose_max_vol = rot_max_vol
print('pose_max_vol = ' + str(pose_max_vol))

#recreating max volume pose
for i in range(finger_index + 1):
    context.active_object.select_set(False)
    view_layer.objects.active = hand_left
    pbone = context.object.pose.bones[bone_num[i]]
    if i != finger_index:
        pbone.rotation_euler[0] = math.radians(-80)
    else:
        pbone.rotation_euler[0] = math.radians(angle)
        view_layer.objects.active = test_object
        #rotate object 
        if rot_index == 0:
            context.active_object.rotation_euler[0] = math.radians(180) #DOWN
        elif rot_index == 1:
            context.active_object.rotation_euler[0] = math.radians(90) #FORWARD
        elif rot_index == 2:
            context.active_object.rotation_euler[0] = math.radians(-90) #BACKWARDS
        elif rot_index == 3:
            context.active_object.rotation_euler[1] = math.radians(-90) #RIGHT
        elif rot_index == 4:
            context.active_object.rotation_euler[1] = math.radians(90) #LEFT 
        #after storing best rotation and max volume, recreate that pose as the final move and print the volume associated
#    

#weird jump in volume when angle is 60 degrees
#set pose here
#get the volume of intersection in the 6 directions
#loop again
 # get volue, rotate, make new mesh, get volume rotate etc

