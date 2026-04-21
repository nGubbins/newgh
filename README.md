# newgh

Sets up a project repo for modern development with python.

Run:
```
newgh MyNewProject
```
## Project scaffold:
```
MyNewProject/
├── src/            # Your source code [Empty]
├── tests/          # Your pytest files [Empty]
├── docs/           # Documentation [Empty]
├── .gitignore      # Standard Python ignores
└── README.md       # Project overview
```

## Default README.md:
```
## Setup Instructions
1. Clone the repo
2. Activate environment: `.\env\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
```

## Default .gitignore:
```
env/
*.pyc
__pycache__/
.DS_Store
.env
.vscode/
.idea/
```

## Next Steps

* **Automated Testing**: Auto-generate default workflows `test_dummy`.
* **Licensing**: Option to create a `LICENSE` file.
* **PyPI Ready**: Option to create a `pyproject.toml` for easy distribution.
