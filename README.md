# Python BDD framework

* Testing framework for black box testing using pytest-bdd, python, selenium

## Pre-requisites
   1. Python / Anaconda / Miniconda 
   2. IDE of your choice (IntelliJ Idea / Pycharm / VS Code etc...)
   3. Chromedriver binary
   4. Git

## Setup environment

### Environment variables (Optional)

      
      $ PIPENV_VENV_IN_PROJECT  =  1          # forces virtual environment creation in project directory
      $ WORKON_HOME = {directory.of.choice}   # forces virtual enviroment in specified directory 


### Install 'pipenv' package manager


      $ pip install pipenv


### Setup 'conda' environment (Optional)
   
Use this step only if you are using lower version of python < 3.9 and wish to upgrade it rather than
installing separately.
However, you can still use `conda` environment + `virtual` environment created using pipenv if you wish to.

        
#### Create conda environment
     

      $ conda create --name py39 python=3.9


#### Activate conda environment
      
      
      # --- If you are using command prompt ---
      $ conda activate py39

      # --- If you are using git bash ---
      $ source activate py39

        
### Create virtual environment using `pipenv` & install packages from Pipfile

#### Navigate to project directory
      

      $ cd {project.dir}


#### Create virtual environment & install packages
      

      $ pipenv --site-packages install --dev --skip-lock


### Verify installation


#### Virtual environment location
      

      $ pipenv --venv


#### Python interpreter location
      
      
      $ pipenv run where python        # Use the python.exe location from virtual environment


#### Check Installed packages
      

      $ pipenv graph

## Setup tests
For this implementation to work, you would need to set an environment variable before you run the tests.
Set the following environment variable. It can accept either `dev` or `prod` as value.


    Environment=(dev|prod)


## Running tests

You can run the tests easily by issuing the following command.

#### Navigate to project directory


      $ cd {project.dir}


#### Running all tests

            
      $ pipenv run pytest


#### Running single python module
      

      $ pipenv run pytest {path to 'test_*.py' file}


#### Running tests using tags


      $ pipenv run pytest -m {tag.name}


## Generate test reports

### Download allure cli

Download the latest version of allure cli from Maven Central (https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)

### Generate report

#### Navigate to the report directory 
See the `--alluredir` flag it is either mentioned in the `pytest.ini` file or using the `PYTEST_ADDOPTS` environment variable.


      $ cd {reports.dir}

#### Generate reports


    $ allure serve json -p 5555



## Useful links
1. [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)
2. [pytest](https://docs.pytest.org/en/latest/contents.html)
3. [allure](https://docs.qameta.io/allure/)