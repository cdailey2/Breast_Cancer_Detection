# This file is used to convert jupyter notebook files to json format in order cleanly merge ipynb files on GitHub

import json

# Path to the notebook file
notebook_path = '/content/your_notebook.ipynb'  # Adjust this path to your notebook's path

# Read the notebook content
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# Convert the notebook content to JSON string
notebook_json = json.dumps(notebook_content, indent=4)

# Print the JSON string
print(notebook_json)

# Copy and paste to intended branch to be merged with main
