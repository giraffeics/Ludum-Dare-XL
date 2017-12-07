blender249 = True
import sys

try: import Blender
except:
	blender249 = False
	import bpy	

if blender249:
	try: import export_fbx
	except:
		print('error: export_fbx not found.')
		Blender.Quit()
else:
	try: import io_scene_fbx.export_fbx
	except:
		print('error: io_scene_fbx.export_fbx not found.')
		# This might need to be bpy.Quit()
		raise

# Accept command line arguments and load the contents of the .blend file
infile = sys.argv[5]
bpy.ops.wm.open_mainfile(filepath=infile)
outfile = sys.argv[6]


# Do the conversion
print("Starting blender to FBX conversion " + outfile)

if blender249:
	mtx4_x90n = Blender.Mathutils.RotationMatrix(-90, 4, 'x')
	export_fbx.write(outfile,
		EXP_OBS_SELECTED=False,
		EXP_MESH=True,
		EXP_MESH_APPLY_MOD=True,
		EXP_MESH_HQ_NORMALS=True,
		EXP_ARMATURE=True,
		EXP_LAMP=True,
		EXP_CAMERA=True,
		EXP_EMPTY=True,
		EXP_IMAGE_COPY=False,
		ANIM_ENABLE=True,
		ANIM_OPTIMIZE=False,
		ANIM_ACTION_ALL=True,
		GLOBAL_MATRIX=mtx4_x90n)
else:
	# blender 2.58 or newer
	import math
	from mathutils import Matrix
	# -90 degrees
	mtx4_x90n = Matrix.Rotation(-math.pi / 2.0, 4, 'X')
	
	print("moo")
	
	class FakeOp:
		def report(self, tp, msg):
			print("%s: %s" % (tp, msg))
	
	exportObjects = ['ARMATURE', 'EMPTY', 'MESH']
		
	minorVersion = bpy.app.version[1];	
	if minorVersion <= 58:
		# 2.58
		io_scene_fbx.export_fbx.save(FakeOp(), bpy.context, filepath=outfile,
			global_matrix=mtx4_x90n,
			use_selection=False,
			object_types=exportObjects,
			mesh_apply_modifiers=True,
			ANIM_ENABLE=True,
			ANIM_OPTIMIZE=False,
			ANIM_OPTIMIZE_PRECISSION=6,
			ANIM_ACTION_ALL=True,
			batch_mode='OFF',	
			BATCH_OWN_DIR=False)
	else:
		# 2.59 and later
		kwargs = io_scene_fbx.export_fbx.defaults_unity3d()
		io_scene_fbx.export_fbx.save(FakeOp(), bpy.context, filepath=outfile, **kwargs)
	# HQ normals are not supported in the current exporter

print("Finished blender to FBX conversion " + outfile)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
blender249 = True
import sys
 
try: import Blender
except:
    blender249 = False
    import bpy    
 
if blender249:
    try: import export_fbx
    except:
        print('error: export_fbx not found.')
        Blender.Quit()
else:
    try: import io_scene_fbx.export_fbx
    except:
        print('error: io_scene_fbx.export_fbx not found.')
        # This might need to be bpy.Quit()
        raise
 
# Accept command line arguments and load the contents of the .blend file
infile = sys.argv[5]
bpy.ops.wm.open_mainfile(filepath=infile)
outfile = sys.argv[6]
 
 
# Do the conversion
print("Starting blender to FBX conversion " + outfile)
 
if blender249:
    mtx4_x90n = Blender.Mathutils.RotationMatrix(-90, 4, 'x')
    export_fbx.write(outfile,
        EXP_OBS_SELECTED=False,
        EXP_MESH=True,
        EXP_MESH_APPLY_MOD=True,
        EXP_MESH_HQ_NORMALS=True,
        EXP_ARMATURE=True,
        EXP_LAMP=True,
        EXP_CAMERA=True,
        EXP_EMPTY=True,
        EXP_IMAGE_COPY=False,
        ANIM_ENABLE=True,
        ANIM_OPTIMIZE=False,
        ANIM_ACTION_ALL=True,
        GLOBAL_MATRIX=mtx4_x90n)
else:
    # blender 2.58 or newer
    import math
    from mathutils import Matrix
    # -90 degrees
    mtx4_x90n = Matrix.Rotation(-math.pi / 2.0, 4, 'X')
    
    print("moo")
    
    class FakeOp:
        def report(self, tp, msg):
            print("%s: %s" % (tp, msg))
    
    exportObjects = ['ARMATURE', 'EMPTY', 'MESH']
        
    minorVersion = bpy.app.version[1];    
    if minorVersion <= 58:
        # 2.58
        io_scene_fbx.export_fbx.save(FakeOp(), bpy.context, filepath=outfile,
            global_matrix=mtx4_x90n,
            use_selection=False,
            object_types=exportObjects,
            mesh_apply_modifiers=True,
            ANIM_ENABLE=True,
            ANIM_OPTIMIZE=False,
            ANIM_OPTIMIZE_PRECISSION=6,
            ANIM_ACTION_ALL=True,
            batch_mode='OFF',    
            BATCH_OWN_DIR=False)
    else:
        # 2.59 and later
        kwargs = io_scene_fbx.export_fbx.defaults_unity3d()
        io_scene_fbx.export_fbx.save(FakeOp(), bpy.context, filepath=outfile, **kwargs)
    # HQ normals are not supported in the current exporter
 
print("Finished blender to FBX conversion " + outfile)