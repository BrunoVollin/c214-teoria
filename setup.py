"""
Setup (build) script for the package.
"""
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
BASE_PLATFORM = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="calculator",
    version="1.0",
    description="My calculator app!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None,
                            target_name="calculator.exe")],
)
