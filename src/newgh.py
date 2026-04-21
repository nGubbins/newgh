import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Helper to run shell commands and catch errors."""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e}")
        sys.exit(1)

def main():
    # 1. Get Project Name from Command Line Arguments
    # sys.argv[0] is the script name, sys.argv[1] is the first word after it
    if len(sys.argv) < 2:
        print("Usage: python setup_project.py <project_name>")
        print("Example: python setup_project.py MyNewApp")
        return

    project_name = sys.argv[1]
    project_path = os.path.join(os.getcwd(), project_name)

    if os.path.exists(project_path):
        print(f"Error: Folder '{project_name}' already exists.")
        return

    print(f"--- Creating project: {project_name} ---")
    os.makedirs(project_path)

    # Additional directories
    # Define the professional folder structure
    folders = ['src', 'tests', 'docs']
    
    for folder in folders:
        folder_full_path = os.path.join(project_path, folder)
        os.makedirs(folder_full_path)
        # Create a hidden '.gitkeep' file so Git tracks the empty folder
        with open(os.path.join(folder_full_path, ".gitkeep"), "w") as f:
            pass

    # 2. Setup Virtual Environment
    print("Setting up virtual environment...")
    run_command("python -m venv env", cwd=project_path)

    # 3. Initialize Git
    print("Initializing Git...")
    run_command("git init", cwd=project_path)

    # 4. Create .gitignore
    print("Creating .gitignore...")
    gitignore_content = """env/
*.pyc
__pycache__/
.DS_Store
.env
.vscode/
.idea/
"""
    with open(os.path.join(project_path, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore_content)

    # 5. Create README.md
    print("Creating README.md...")
    readme_content = f"""# {project_name}

Project scaffold.

## Setup Instructions
1. Clone the repo
2. Activate environment: `.\\env\\Scripts\\activate`
3. Install dependencies: `pip install -r requirements.txt`
"""
    with open(os.path.join(project_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 5.5 Create an empty requirements.txt
    print("Creating requirements.txt...")
    with open(os.path.join(project_path, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write("# List your project dependencies here\n")
    
    # 6. First Commit
    print("Performing initial commit...")
    run_command("git add .", cwd=project_path)
    run_command('git commit -m "chore: initial project scaffolding"', cwd=project_path)

    # 7. GitHub Integration
    print(f"Creating private GitHub repo: {project_name}...")
    # Using the dynamic project_name variable here
    run_command(f"gh repo create {project_name} --private --source=. --remote=origin", cwd=project_path)
    
    # Modern Git often defaults to 'main'. If yours uses 'master', change it here.
    print("Pushing to GitHub...")
    run_command("git push -u origin master", cwd=project_path)

    print(f"\n--- Success! ---")
    print(f"Next steps:")
    print(f"1. cd {project_name}")
    print(f"2. .\\env\\Scripts\\activate")

if __name__ == "__main__":
    main()