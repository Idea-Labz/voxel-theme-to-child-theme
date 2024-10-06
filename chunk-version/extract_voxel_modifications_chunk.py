import os
import shutil

def compare_files(file1, file2, buffer_size=8192):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            b1 = f1.read(buffer_size)
            b2 = f2.read(buffer_size)
            if b1 != b2:
                return False
            if not b1:
                return True

def extract_modifications(original_dir, modified_dir, child_dir):
    for root, dirs, files in os.walk(modified_dir):
        rel_path = os.path.relpath(root, modified_dir)
        
        for file in files:
            modified_file = os.path.join(root, file)
            original_file = os.path.join(original_dir, rel_path, file)
            child_file = os.path.join(child_dir, rel_path, file)
            
            if os.path.exists(original_file):
                if not compare_files(original_file, modified_file):
                    os.makedirs(os.path.dirname(child_file), exist_ok=True)
                    shutil.copy2(modified_file, child_file)
                    print(f"Extracted modified file: {child_file}")
            else:
                os.makedirs(os.path.dirname(child_file), exist_ok=True)
                shutil.copy2(modified_file, child_file)
                print(f"Extracted new file: {child_file}")

# Set the paths for your themes
original_theme_path = "voxel-original"
modified_theme_path = "voxel"
child_theme_path = "voxel-child"

# Run the extraction process
extract_modifications(original_theme_path, modified_theme_path, child_theme_path)