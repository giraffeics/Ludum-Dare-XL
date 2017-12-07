@echo off
blender --background --python "%cd%\blendToFbxExporter.py" -- "%cd%\args-Unity-BlenderToFBX.py" "%cd%\..\Assets"
pause