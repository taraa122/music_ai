import numpy as np
import os

# Directory containing .npy files
npy_dir = 'data/npy/'

def check_npy_shapes(directory):
    """
    Check the shape of all .npy files in the given directory.
    
    :param directory: Directory containing .npy files.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.npy'):
            file_path = os.path.join(directory, filename)
            try:
                data = np.load(file_path)
                print(f"File: {filename} - Shape: {data.shape}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")

if __name__ == '__main__':
    check_npy_shapes(npy_dir)
