# Codex Demo Sandbox

-----

## Stack

- Unix-type environment (MacOS, RPM-based, Debian-based, etc.)
- Python 3.13

-----

## Setup

1. Open a Terminal.
2. Navigate to your project's directory.
3. Enter the following commands:

    ```sh
    # Create a Python 3.13 virtual environment
    python3.13 -m venv .venv
    # Activate the environment
    source .venv/bin/activate
    python --version
    # Install a Python package manager
    python -m pip install --upgrade pip
    # Install a linter and style checker
    python -m pip install pylint autopep8
    python -m pip freeze > requirements.txt
    ```

4. Using an editor of your choice, create a autopep8 configuration file named `.pep8` in the project's directory with the following content:

    ```ini
    [pep8]
    exclude = .venv/*
    ```

5. Add a `.pylintrc` file with the following content as well:

    ```ini
    [MAIN]
    ignore=.venv
    ```

    > **NOTES**
    >
    > - If you are using Visual Studio Code, you can add a `.vscode` directory containing a `settings.json` file with your desired settings (see <https://github.com/garciart/pensieve/blob/main/settings.json> for an example). Just remember to add the new directory and any other directories you do not want checked by autopep8 or pylint to their `.pep8` and `.pylintrc` configuration files, respectively (e.g., `exclude = .venv/*, .vscode/*`).
    >
    > - You can replace autopep8 with a style-checker of your choice (e.g., Flake8, Black, etc.). pylint actually uses PEP8, so style-checking with autopep8 is redundant. I included it to demonstrate configuring and performing linting and style checking.

6. Add a `.gitignore` file to prevent Git from interacting with certain files, like the `.venv` directory. You can get a `.gitignore` file for Python projects from GitHub at <https://github.com/github/gitignore/blob/main/Python.gitignore>. You may also download the file to the project's root directory: `curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore`.
7. Ensure `.venv` and `.vscode/` are present and uncommented in your `.gitignore` file.
8. Ensure `.pylintrc` and `.pep8` are also present and uncommented in your `.gitignore` file.
9. Copy your `.gitignore` to a file named `.codexignore`. That will prevent Codex from interacting with those files and folders.

    > **NOTE** - You may add additional files and folders you do not want Git or Codex to touch to your `.gitignore` and `.codexignore` files, respectively, as needed while you work on your project (e.g., `.scratch/`, etc.).

10. 
