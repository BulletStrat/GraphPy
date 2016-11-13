import cx_Freeze
import sys

import matplotlib

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable("UserInterface.py",base=base, icon='app.ico')]

cx_Freeze.setup(
    name = 'GraphPy',
    options = {"build_exe": {"packages":["numpy","PyQt5","DataAnalyzer", "matplotlib","GraphVariables","pandas",],
                             "include_files":["app.ico", "DataAnalyzer.py","GraphVariables.py"]}},
    version = "1.00",
    description = "Graph data",
    executables = executables
)