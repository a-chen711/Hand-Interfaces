import bpy
import math
import bmesh
gesture = 1


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
lh_volume = bm_left.calc_volume() - 0.00733 #approximate forearm volume
print('LH Mesh Volume = ' + str(lh_volume))
#bm_left.faces.ensure_lookup_table() #allows iteration of faces
#verts = bm_left.faces[-1].verts[:]
#print(verts)
#for v in bm_left.verts:
#    print(v.co)
#print(bm_left.verts.calc_edge_angle())

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
    pbone.rotation_euler[0] = math.radians(0)
    pbone.rotation_euler[1] = math.radians(80.5)
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
    pbone.rotation_euler[0] = math.radians(0)
    pbone.rotation_euler[1] = math.radians(80.5)
    pbone.rotation_euler[2] = math.radians(0)

#overlaying Sphere on top of hand
context.active_object.select_set(False)
view_layer.objects.active = sphere
so = bpy.context.active_object
m_sphere = bmesh_copy_from_object(sphere, apply_modifiers=True)
volume = m_sphere.calc_volume()
print('Sphere Mesh Volume = ' + str(volume))
#so.location = (0.87 -0.10, 0)

sphere = scene.objects.get("Sphere")
bpy.ops.object.modifier_add(type = 'BOOLEAN')
context.object.modifiers["Boolean"].operation = 'INTERSECT'            
bpy.context.object.modifiers["Boolean"].object = lh_mesh

context.active_object.select_set(False)
view_layer.objects.active = sphere
m_sphere = bmesh_copy_from_object(sphere, apply_modifiers=True)
volume = m_sphere.calc_volume()
m_sphere.free()
print('Sphere Mesh Volume = ' + str(volume))
error = volume/lh_volume * 100
print('Percentage Similarity by Volume = ' + str(error))
#Account for forearm error when only using hands

