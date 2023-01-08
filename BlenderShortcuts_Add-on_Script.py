bl_info = {
    "name": "Blender Shortcuts",
    "author": "Kion",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbar > Blender Shortcuts",
    "description": "Adds objects and other functions to help our workflow (Tutorial Result)",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy

    #This is the Main Panel (Parent of Panel A and B)
class MainPanel(bpy.types.Panel):
    bl_label = "Blender Shortcuts"
    bl_idname = "PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderShortcuts'
   
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2
       
        row = layout.row()
        row.label(text= "Add the...")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text= "Cube")       

      #This is Panel B - The Scale Sub Panel (Child of MainPanel)
class PanelA(bpy.types.Panel):
    bl_label = "Add"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderShortcuts'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}
   
    def draw(self, context):
        layout = self.layout
        obj = context.object
       
        row = layout.row()
        row.label(text= "Add objects:")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text= "Cube")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", text= "Sphere")
        row = layout.row()
        row.operator("mesh.primitive_monkey_add", text= "Suzanne")
        row = layout.row()
        row.operator("mesh.primitive_plane_add", text= "Plane")
        row = layout.row()
        row.operator("mesh.primitive_cylinder_add", text= "Cylinder")
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", text= "Ico Sphere")
        row = layout.row()
        row.operator("mesh.primitive_cone_add", text= "Cone")
        row = layout.row()
        row.label(text= "Add Curves:")
        row = layout.row()
        row.operator("curve.primitive_bezier_curve_add", text= "Bezier Curve")
        row.operator("curve.primitive_bezier_circle_add", text= "Bezier Circle")
        row = layout.row()
        row.label(text= "Add Lights:")
        row = layout.row()
        row.operator("object.light_add", text= "Add Light")
        row = layout.row()
        row.label(text= "Add a Camera:")
        row = layout.row()
        row.operator("object.camera_add", text= "Add Camera")
        row = layout.row()
        row.operator("view3d.camera_to_view", text= "Possition active Camera to view")
        



    #This is Panel B - The Scale Sub Panel (Child of MainPanel)
class PanelB(bpy.types.Panel):
    bl_label = "Other Options"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderShortcuts'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}
   
    def draw(self, context):
        layout = self.layout
        obj = context.object
       
        row = layout.row()
        row.label(text= "Scale the object:")
        row = layout.row()
        row.operator("transform.resize", text= "Scale")
        row = layout.row()
        layout.scale_y = 1.2
       
        col = layout.column()
        col.prop(obj, "scale")
        
        row = layout.row()
        row.label(text= "> Select a Option")
        row = layout.row()
        row.operator("object.shade_smooth", icon= 'MOD_SMOOTH', text= "Set Smooth Shading")
        row.operator("object.subdivision_set", icon= 'MOD_SUBSURF', text= "Add Subsurf")
        row = layout.row()
        
        row.operator("object.modifier_add", icon= 'MODIFIER')
        row = layout.row()
        row.label(text= "Camera:")
        row = layout.row()
        row.operator("view3d.camera_to_view", text= "Position active Camera to view")
        row = layout.row()
        row.operator("cameras['Camera.007'].lens", text= "Focal Length")
        row = layout.row()
        row.operator("object.data.dof.use_dof = True", text= "Depth of Field ON/OFF")
        row = layout.row()
        row.label(text= "Delete")
        row = layout.row()
        row.operator("object.delete", text="Delete")
        
        bpy.data.cameras['Camera.007'].lens

    #This is Panel C - The Scale Sub Panel (Child of MainPanel)
class PanelC(bpy.types.Panel):
    bl_label = ".Blend Properties"
    bl_idname = "PT_PanelC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderShortcuts'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}
   
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.operator("wm.save_mainfile", text="Save Blend File")
        row = layout.row()
        row.operator("wm.append", text="Append")
        
    #This is Panel D - The Scale Sub Panel (Child of MainPanel)
class PanelD(bpy.types.Panel):
    bl_label = "Export Options"
    bl_idname = "PT_PanelD"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Adder'
    bl_parent_id = 'PT_MainPanel'
    bl_options = {'DEFAULT_CLOSED'}
   
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text= "Export")
        row = layout.row()
        row.operator("export_scene.fbx", text="Export as FBX")
        row = layout.row()
        row.operator("wm.collada_export", text="Export as dae")
        row = layout.row()
        row.operator("export_mesh.stl", text="Export as STL")
        row = layout.row()
        row.operator("export_scene.obj", text="Export as .obj")
        
        
        
            #This is the Second Panel (Parent of Panel A and B)
class SecondPanel(bpy.types.Panel):
    bl_label = "World Settings"
    bl_idname = "PT_SecondPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderShortcuts'
   
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2
       
        row = layout.row()
        row.label(text= "setting unavalible")
        row = layout.row()
        row.operator("bpy.data.worlds['World'].node_tree.nodes['Background'].inputs[1].default_value")
       
    #Here we are Registering the Classes       
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(SecondPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    bpy.utils.register_class(PanelC)
    bpy.utils.register_class(PanelD)

    #Here we are UnRegistering the Classes   
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(SecondPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    bpy.utils.unregister_class(PanelC)
    bpy.utils.unregister_class(PanelD)

    #This is required in order for the script to run in the text editor   
if __name__ == "__main__":
    register() 