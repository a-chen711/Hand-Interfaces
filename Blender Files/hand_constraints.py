import bpy
import math

def main(context):
    for ob in context.scene.objects:
        print(ob)


class ConstraintOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.h_constraints"
    bl_label = "Hand Constraint Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        view_layer = bpy.context.view_layer
        context = bpy.context
        hand_left = bpy.data.objects['Hand_Left']
        hand_right = bpy.data.objects['Hand_Right']
        
        #Hardcoded constraints for each of the bones 
        for x in range(2):
            context.active_object.select_set(False)
            if x == 0:
                hand_left.select_set(True)
                view_layer.objects.active = hand_left
            if x == 1:
                hand_right.select_set(True)
                view_layer.objects.active = hand_right

            bpy.context.object.pose.bones["index control"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.001"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.002"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Major control"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.003"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.004"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.005"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Ring control"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.006"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.007"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.008"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Pinky control"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.009"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.010"].constraints["Limit Rotation"].use_limit_x = True
            bpy.context.object.pose.bones["Bone.011"].constraints["Limit Rotation"].use_limit_x = True


            bpy.context.object.pose.bones["index control"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.001"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.002"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Major control"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.003"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.004"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.005"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Ring control"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.006"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.007"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.008"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Pinky control"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.009"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.010"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            bpy.context.object.pose.bones["Bone.011"].constraints["Limit Rotation"].owner_space = 'LOCAL'
            
            #Setting Initial Rotation
            if x == 0:
                bpy.ops.object.mode_set(mode='POSE')
                xaxis = 0
                yaxis = 1
                zaxis = 2
                pbone = context.object.pose.bones['index control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(-9.5)
                pbone.rotation_euler[zaxis] = math.radians(-2.55)
                pbone = context.object.pose.bones['Major control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(-0.653)
                pbone.rotation_euler[zaxis] = math.radians(-2.55)
                pbone = context.object.pose.bones['Ring control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(-0.657)
                pbone.rotation_euler[zaxis] = math.radians(1.21)
                pbone = context.object.pose.bones['Pinky control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(-7.55)
                pbone.rotation_euler[zaxis] = math.radians(3.78)
            elif x == 1:
                bpy.ops.object.mode_set(mode='POSE')
                xaxis = 0
                yaxis = 1
                zaxis = 2
                pbone = context.object.pose.bones['index control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(1.05)
                pbone.rotation_euler[zaxis] = math.radians(3.85)
                pbone = context.object.pose.bones['Major control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(-0.653)
                pbone.rotation_euler[zaxis] = math.radians(0)
                pbone = context.object.pose.bones['Ring control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(3.51)
                pbone.rotation_euler[zaxis] = math.radians(-0.404)
                pbone = context.object.pose.bones['Pinky control']
                pbone.rotation_euler[xaxis] = math.radians(0)
                pbone.rotation_euler[yaxis] = math.radians(1.67)
                pbone.rotation_euler[zaxis] = math.radians(-2.77)
                
            #Setting Rotation Constraints

            #Thumb


            #Index
            bpy.context.object.pose.bones["index control"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["index control"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.001"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.001"].constraints["Limit Rotation"].min_x = -1.74533

            bpy.context.object.pose.bones["Bone.002"].constraints["Limit Rotation"].max_x = 0.174533
            bpy.context.object.pose.bones["Bone.002"].constraints["Limit Rotation"].min_x = -1.5708


            #Middle
            bpy.context.object.pose.bones["Major control"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Major control"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.003"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.003"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.004"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.004"].constraints["Limit Rotation"].min_x = -1.74533

            bpy.context.object.pose.bones["Bone.005"].constraints["Limit Rotation"].max_x = 0.174533
            bpy.context.object.pose.bones["Bone.005"].constraints["Limit Rotation"].min_x = -1.5708

            #Ring
            bpy.context.object.pose.bones["Ring control"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Ring control"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.006"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.006"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.007"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.007"].constraints["Limit Rotation"].min_x = -1.74533

            bpy.context.object.pose.bones["Bone.008"].constraints["Limit Rotation"].max_x = 0.349066
            bpy.context.object.pose.bones["Bone.008"].constraints["Limit Rotation"].min_x = -1.5708

            #Pinky
            bpy.context.object.pose.bones["Pinky control"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Pinky control"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.009"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.009"].constraints["Limit Rotation"].min_x = -1.39626

            bpy.context.object.pose.bones["Bone.010"].constraints["Limit Rotation"].max_x = 0
            bpy.context.object.pose.bones["Bone.010"].constraints["Limit Rotation"].min_x = -1.74533

            bpy.context.object.pose.bones["Bone.011"].constraints["Limit Rotation"].max_x = 0.523599
            bpy.context.object.pose.bones["Bone.011"].constraints["Limit Rotation"].min_x = -1.5708
        print("Constraints and Rotation Reset")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ConstraintOperator)


def unregister():
    bpy.utils.unregister_class(ConstraintOperator)


if __name__ == "__main__":
    register()

#bpy.ops.object.h_constraints()