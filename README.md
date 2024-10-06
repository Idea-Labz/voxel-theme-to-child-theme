# Voxel Theme Modification Extractor

This project contains two Python scripts to help WordPress theme developers extract their modifications to the Voxel theme by automatically creating a child theme with only the modified files. Both scripts compare the original Voxel theme with a modified version and copy the changed or new files to a child theme directory, maintaining the correct folder structure.

## Project Structure

```
voxel-theme-modifier/
├── README.md
├── standard-version/
│   ├── extract_voxel_modifications.py
│   └── README.md
├── chunk-version/
│   ├── extract_voxel_modifications_chunk.py
│   └── README.md
├── themes/
│   ├── voxel-original/
│   ├── voxel/
│   └── voxel-child/
```

## Features

- Compares files between the original Voxel theme and a modified version
- Identifies new files added to the modified theme
- Extracts only modified or new files to the child theme directory
- Maintains the correct folder structure in the child theme
- Provides console output for extracted files

## Prerequisites

- Python 3.x installed on your system
- Access to the original Voxel theme files
- A copy of the Voxel theme with your modifications
- The original Voxel theme files in a folder called `themes/voxel-original`
- The modified Voxel theme files in a folder called `themes/voxel` 
- The child theme files in a folder called `themes/voxel-child` that can be downloaded from https://docs.getvoxel.io/articles/voxel-child-theme/

## Important Note

Ensure that the Voxel theme versions in both the `themes/voxel-original` and `themes/voxel` directories are the same. This is crucial for accurate comparison and child theme generation. You can download older versions of the Voxel theme from your Voxel account:

1. Log in to your Voxel account
2. Go to Orders
3. Click on Downloads
4. Look for "Recent releases" which contains a list of about 10 previous versions with download links

Using matching versions ensures that the script accurately identifies your modifications and doesn't mistake version differences for custom changes.

## Setup

1. Clone or download this repository to your local machine.
2. Create the following folder structure if it doesn't exist:
   ```
   voxel-theme-modifier/
   └── themes/
       ├── voxel-original/
       ├── voxel/
       └── voxel-child/
   ```
3. Place the original Voxel theme files in the `themes/voxel-original` directory.
4. Place your modified Voxel theme files in the `themes/voxel` directory.
5. Download the Voxel child theme from https://docs.getvoxel.io/articles/voxel-child-theme/ and place its contents in the `themes/voxel-child` directory.
6. Verify that the Voxel theme versions in `themes/voxel-original` and `themes/voxel` are the same.

## Usage

Choose either the standard version or the chunk version based on your needs:

### Standard Version

See the [README.md in the `standard-version` folder](standard-version/README.md) for specific instructions.

### Chunk Version

See the [README.md in the `chunk-version` folder](chunk-version/README.md) for specific instructions.

## Best Practices

- Always keep a backup of your original and modified Voxel theme files.
- Run these scripts in a development environment before applying changes to a live site.
- After generating the child theme, review the copied files to ensure all necessary modifications are included.
- Use version control (e.g., Git) to track changes in your modified Voxel theme and generated child theme.

## Customization

You can modify either script to use different directory names by changing the variables at the bottom of the respective Python files. By default, they are set to:

```python
original_theme_path = "themes/voxel-original"
modified_theme_path = "themes/voxel"
child_theme_path = "themes/voxel-child"
```

Make sure to update these paths if you change the folder structure.
