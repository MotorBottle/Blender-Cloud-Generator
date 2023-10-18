import bpy
import random
import os

def create_cloud_metaballs(name, count, scale, location):
    # Create a new metaball object
    mb = bpy.data.metaballs.new(name)
    obj = bpy.data.objects.new(name, mb)
    bpy.context.collection.objects.link(obj)
    
    # Add individual balls to the metaball object to create cloud shape
    for i in range(count):
        element = mb.elements.new()
        element.co = (random.uniform(-2, 2), random.uniform(-1, 1), random.uniform(-1, 1))
        element.radius = random.uniform(0.5, 1.5)
    
    # Set the cloud scale and location
    obj.scale = scale
    obj.location = location

    # Set the cloud object as the active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Convert metaballs to mesh and get the new mesh object
    bpy.ops.object.convert(target='MESH')
    mesh_obj = bpy.context.active_object

    return mesh_obj

def export_and_delete(obj, filepath):
    # Select the object
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    
    # Export as .fbx
    bpy.ops.export_scene.fbx(filepath=filepath, use_selection=True)
    
    # Delete the object
    bpy.data.objects.remove(obj, do_unlink=True)

def generate_and_export_clouds(num_clouds, base_filepath):
    for i in range(num_clouds):
        cloud_name = f"Cloud_{i}"
        obj = create_cloud_metaballs(cloud_name, 100, (2, 2, 2), (0, 0, 0))
        export_filepath = os.path.join(base_filepath, f"{cloud_name}.fbx")
        export_and_delete(obj, export_filepath)

# Usage
# Replace 'C:/path/to/directory/' with the directory you want to export the .fbx files to
generate_and_export_clouds(10, 'C:/Users/Ccrrq/Documents/clouds')
