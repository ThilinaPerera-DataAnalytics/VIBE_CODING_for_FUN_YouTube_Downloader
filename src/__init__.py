# src/__init__.py

# This file marks the 'src' directory as a Python package.

# You can optionally import modules to make them directly available
# when someone imports the 'src' package.
# For example, to allow 'from src import download_video':
# from .downloader import download_video, download_audio, download_merged

# Alternatively, you can make the entire downloader module available
# at the package level, so you can do 'from src import downloader'.
from . import downloader

# The `__all__` variable is a list of strings that defines what modules
# should be imported when a user does `from src import *`. It's a good
# practice to define this to control the public API of your package.
__all__ = ["downloader"]
