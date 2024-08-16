import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.audio_utils import process_audio
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")
