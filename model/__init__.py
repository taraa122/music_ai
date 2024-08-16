"""
Model package initialization.

This file is used to initialize the model package and can include any
setup code needed for the model components.
"""

from .model import create_model, load_model_from_file
from .train import train_model
from .generate import generate_music
