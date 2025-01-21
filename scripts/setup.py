import os

# Define the folder structure
structure = [
    'backend/',
    'backend/app/',
    'backend/app/api/',
    'backend/app/api/endpoints/',
    'backend/app/api/dependencies/',
    'backend/app/api/__init__.py',
    'backend/app/core/',
    'backend/app/models/',
    'backend/app/services/',
    'backend/app/utils/',
    'backend/app/schemas/',
    'backend/app/main.py',
    'backend/tests/',
    'backend/tests/unit/',
    'backend/tests/integration/',
    'backend/tests/conftest.py',
    'backend/scripts/',
    'backend/migrations/',
    'backend/.github/',
    'backend/.github/copilotinstructions.md',
    'backend/requirements.txt',
    'backend/README.md'
]

# Function to create the directories and files
def create_structure(structure):
    for path in structure:
        if path.endswith('/'):
            os.makedirs(path, exist_ok=True)
        else:
            with open(path, 'w') as f:
                pass

# Start creating the directory structure
create_structure(structure)

print("Project structure created successfully!")
