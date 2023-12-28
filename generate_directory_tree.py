import os

def generate_tree(path, level=0, skip_dirs=None):

    # Create an empty string to hold the directory tree representation
    tree = ''
    # If the current level is 0, add the base directory name to the tree
    if level == 0:
        tree += f'{os.path.basename(path)}\n'
    
    # Iterate over the items in the current directory, sorted alphabetically
    for item in sorted(os.listdir(path)):
        # Get the full path of the item
        item_path = os.path.join(path, item)
        # Skip directories in the skip_dirs set
        if os.path.basename(item_path) in skip_dirs:
            continue

        # If the item is a directory, add it to the tree and recursively call the function with the new path
        if os.path.isdir(item_path):
            # Add the directory name to the tree, with appropriate indentation based on the current level
            tree += '│   ' * level + f'├── {item}/\n'
            # Recursively call the function with the new path, incrementing the level
            tree += generate_tree(item_path, level + 1, skip_dirs)
        # If the item is a file, add it to the tree with appropriate indentation
        else:
            tree += '│   ' * level + f'├── {item}\n'
    
    # Return the complete directory tree representation
    return tree

# Set the root directory for the directory tree
root_directory = '/mnt/c/Users/RuanLima/SBF/ORACLE-MFP'

# You can now easily add other directories to skip
skip_directories = {'.git', 'node_modules', 'venv', '.github'}

# Print the directory tree for the root directory
print(generate_tree(root_directory, skip_dirs=skip_directories))
