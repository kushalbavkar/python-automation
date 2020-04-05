from pytest_bdd.steps import given

@given('test cucumber')
def sample():
    print(f'called from sample.py')
    pass