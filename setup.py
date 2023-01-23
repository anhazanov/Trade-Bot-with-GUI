import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico', 'themes/', 'Exchanges/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Futures trade",
    version = "1.0",
    description = "Futures trade (test app)",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
