from cx_Freeze import setup,Executable

includefiles = []

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(
    name = 'Snake',
    version = '1.0',
    description = 'Snake clone in python',
    author = 'Lennart Buit',
    options = {"build_exe": build_exe_options}, 
	executables = [Executable(script="game.py", base = None, targetName="Snake.exe")]
)
