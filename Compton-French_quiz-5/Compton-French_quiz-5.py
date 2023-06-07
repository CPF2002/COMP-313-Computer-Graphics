'''
Student Name: Compton French
Student Partner: YourPartnerFirstName YourParnterLastName
COMP 313: Computer Graphics Fall 2022
'''

import bpy
import bmesh

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# create all the objects
# cube 1
bpy.ops.mesh.primitive_cube_add(radius=1, location=(-3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")
bm = bmesh.from_edit_mesh(bpy.context.object.data)
# select correct face and scale 0.5
bm.faces.ensure_lookup_table()
bm.faces[4].select = True
bpy.ops.transform.resize(value = (0.5, 0.5, 0.5))
bpy.ops.object.mode_set(mode='OBJECT')

# cube 2
bpy.ops.mesh.primitive_cube_add(radius=1, location=(3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")
bm = bmesh.from_edit_mesh(bpy.context.object.data)
# select correct face and scale 0.5
bm.faces.ensure_lookup_table()
bm.faces[4].select = True
bpy.ops.transform.resize(value = (0.5, 0.5, 0.5))
bpy.ops.object.mode_set(mode='OBJECT')

# monkey 1
bpy.ops.mesh.primitive_monkey_add(radius=1, location=(-3, 0, 2))
# rotate correctly
bpy.ops.transform.rotate(value = 1.5, axis = (0, 0, 1))

# monkey 2
bpy.ops.mesh.primitive_monkey_add(radius=1, location=(3, 0, 2))
# rotate correctly
bpy.ops.transform.rotate(value = -1.5, axis = (0, 0, 1))
