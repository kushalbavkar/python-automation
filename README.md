## Python BDD for testing using pytest-bdd

* Testing framework for black box testing using pytest-bdd, python, selenium

### Pre requisites
1. Python >= 3.7 or Anaconda
2. IDE of your choice (Pycharm / VS Code etc..)
3. Chromedriver binary
4. Git

### Setup environment
1. Set the below environment variables on your system

    * PIPENV_VENV_IN_PROJECT="enabled" : sets up pipenv virtual environment in project directory
    * PYTHONDONTWRITEBYTECODE=1 : prevents pytest from creating `__pycache__` folders

2. Install dependencies and create pipenv virtual environment
    * Upgrade to python version 3.7 if you have a lower version & if you are using Anaconda distribution using the below command

        `conda create --name py37 python=3.7` => creates conda environment 

        `conda activate py37` => command prompt 

        `source activate py37` => bash

        (`Note`: if you are using this setup then you would need to activate the environment before proceeding with the next steps.. use conda activate or source activate commands mentioned above)

    * Create virtual environment and install dependencies. Navigate to the project directory and enter the below commands

        `pip install pipenv` => use this only for the first time while setting up the virtual enviroment

        `pipenv install --dev --skip-lock` => use this command whenever you have changed the dependencies in Pipfile


### Useful links
1. https://github.com/pytest-dev/pytest-bdd
2. https://readthedocs.org/projects/pytest-bdd/downloads/pdf/latest/
3. https://docs.pytest.org/en/latest/contents.html
