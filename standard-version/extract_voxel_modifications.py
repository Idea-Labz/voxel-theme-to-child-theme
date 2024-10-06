import os
import filecmp
import shutil

def compare_and_copy(original_dir, modified_dir, child_dir):
    for root, dirs, files in os.walk(modified_dir):
        # Get the relative path
        rel_path = os.path.relpath(root, modified_dir)
        
        for file in files:
            modified_file = os.path.join(root, file)
            original_file = os.path.join(original_dir, rel_path, file)
            child_file = os.path.join(child_dir, rel_path, file)
            
            # Check if the file exists in the original theme
            if os.path.exists(original_file):
                # Compare the files
                if not filecmp.cmp(original_file, modified_file, shallow=False):
                    # If files are different, copy to child theme
                    os.makedirs(os.path.dirname(child_file), exist_ok=True)
                    shutil.copy2(modified_file, child_file)
                    print(f"Copied modified file: {child_file}")
            else:
                # If the file doesn't exist in the original theme, it's a new file
                os.makedirs(os.path.dirname(child_file), exist_ok=True)
                shutil.copy2(modified_file, child_file)
                print(f"Copied new file: {child_file}")

# Set the paths for your themes
original_theme_path = "voxel-original"
modified_theme_path = "voxel"
child_theme_path = "voxel-child"

# Run the comparison and copy process
compare_and_copy(original_theme_path, modified_theme_path, child_theme_path)