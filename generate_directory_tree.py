import os

# Define a function that generates a textual representation of the directory tree
def generate_tree(path, level=0):
    # Create an empty string to hold the directory tree representation
    tree = ''
    # If the current level is 0, add the base directory name to the tree
    if level == 0:
        tree += f'{os.path.basename(path)}\n'
    
    # Iterate over the items in the current directory, sorted alphabetically
    for item in sorted(os.listdir(path)):
        # Get the full path of the item
        item_path = os.path.join(path, item)
        # If the item is a directory, add it to the tree and recursively call the function with the new path
        if os.path.isdir(item_path):
            # Add the directory name to the tree, with appropriate indentation based on the current level
            tree += '│   ' * level + f'├── {item}/\n'
            # Recursively call the function with the new path, incrementing the level
            tree += generate_tree(item_path, level + 1)
        # If the item is a file, add it to the tree with appropriate indentation
        else:
            tree += '│   ' * level + f'├── {item}\n'
    
    # Return the complete directory tree representation
    return tree

# Set the root directory for the directory tree
root_directory = '/home/ruan/Music/lista_criativa'

# Print the directory tree for the root directory
print(generate_tree(root_directory))
