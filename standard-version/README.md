# Standard Voxel Theme Modification Extractor

This Python script helps extract modifications made to the Voxel theme using a standard file comparison method.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the `standard-version` directory.
3. Run the script using Python:
   ```
   python extract_voxel_modifications.py
   ```
4. The script will compare the files in `voxel-original` and `voxel`, copying modified or new files to `voxel-child`.
5. Check the console output to see which files were extracted to the child theme.

## How It Works

1. The script goes through all files in the modified `voxel` directory.
2. For each file, it checks if a corresponding file exists in the `voxel-original` directory.
3. If the file exists in both directories, it compares the contents using `filecmp.cmp()`:
   - If the contents are different, the file is copied to the `voxel-child` directory.
   - If the contents are the same, the file is skipped.
4. If a file exists in the modified `voxel` directory but not in `voxel-original`, it's considered a new file and is copied to `voxel-child`.
5. The script maintains the original folder structure when copying files to `voxel-child`.

Note: This version uses `filecmp.cmp()` for file comparison, which may not be the most efficient for very large files.