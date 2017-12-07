
#
# blendToFbxExporter.py
#
# Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
# http://blog.kzarczynski.com/
# Copyright (c) 2015 Krzysztof Żarczyński. All rights reserved.
#	

#
# The script exports multiple files from Blender into fbx models. 
# It searches the path recursively and creates .fbx files next to the .blend files,
# then it renames corresponding Unity *.blend.meta files to *.fbx.meta to keep editor references,
# !!! then it deletes the .blend files !!!
# You need Blender to be installed on your machine. 
# You need to specify the following command line arguments: 
# Blender's directory, path to args-Unity-BlenderToFBX.py, input directory (with blend files) 
#

import os
import os.path
import sys
import glob
import bpy
import fnmatch
import subprocess

if len(sys.argv) != 7:
    print("\nusage:  --background --python  --   ")
else:
    pathToBlender = sys.argv[0]
    pathToBlenderToFBX = sys.argv[5]
    path = sys.argv[6]
    alreadyHaveFBX = []
    processedFiles = []
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend')]
    for infile in configfiles:
        outfilename = infile.replace('blend', 'fbx')
        if os.path.isfile(outfilename):
            alreadyHaveFBX.append(infile)
        else:
            status = subprocess.call(pathToBlender + ' --background --python ' + pathToBlenderToFBX + '  -- "' + infile + '" "' + outfilename + '"');
            os.remove(infile)
            processedFiles.append(infile)
        
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend.meta')]
    for infile in configfiles:
        outfilename = infile.replace('blend', 'fbx')
        if not os.path.isfile(outfilename):
            os.rename(infile, outfilename)

    print("Processed files:")
    print(len(processedFiles))
    print("Skipped files (.fbx already exists at the locaton):")
    print(len(alreadyHaveFBX))
    for infile in alreadyHaveFBX:
        print(infile)
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
#
# blendToFbxExporter.py
#
# Created by Krzysztof Żarczyński (@iamsed) on 16.11.15.
# http://blog.kzarczynski.com/
# Copyright (c) 2015 Krzysztof Żarczyński. All rights reserved.
#    
 
#
# The script exports multiple files from Blender into fbx models. 
# It searches the path recursively and creates .fbx files next to the .blend files,
# then it renames corresponding Unity *.blend.meta files to *.fbx.meta to keep editor references,
# !!! then it deletes the .blend files !!!
# You need Blender to be installed on your machine. 
# You need to specify the following command line arguments: 
# Blender's directory, path to args-Unity-BlenderToFBX.py, input directory (with blend files) 
#
 
import os
import os.path
import sys
import glob
import bpy
import fnmatch
import subprocess
 
if len(sys.argv) != 7:
    print("\nusage:  --background --python  --   ")
else:
    pathToBlender = sys.argv[0]
    pathToBlenderToFBX = sys.argv[5]
    path = sys.argv[6]
    alreadyHaveFBX = []
    processedFiles = []
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend')]
    for infile in configfiles:
        outfilename = infile.replace('blend', 'fbx')
        if os.path.isfile(outfilename):
            alreadyHaveFBX.append(infile)
        else:
            status = subprocess.call(pathToBlender + ' --background --python ' + pathToBlenderToFBX + '  -- "' + infile + '" "' + outfilename + '"');
            os.remove(infile)
            processedFiles.append(infile)
        
    configfiles = [os.path.join(dirpath, f) 
    for dirpath, dirnames, files in os.walk(path) 
    for f in fnmatch.filter(files, '*.blend.meta')]
    for infile in configfiles:
        outfilename = infile.replace('blend', 'fbx')
        if not os.path.isfile(outfilename):
            os.rename(infile, outfilename)
 
    print("Processed files:")
    print(len(processedFiles))
    print("Skipped files (.fbx already exists at the locaton):")
    print(len(alreadyHaveFBX))
    for infile in alreadyHaveFBX:
        print(infile)