from pytest_bdd import scenario
import allure


@allure.tag('UI')
@allure.epic('GitHub')
@allure.parent_suite('GitHub')
@allure.suite('GitHub sanity checks')
@allure.sub_suite('GitHub project search')
@allure.title('Verify presence of pytest-bdd project')
@allure.description('Verify presence of pytest-bdd project under pytest-dev user profile')
@scenario('github.feature', 'Verify presence of pytest-bdd project')
def test_verify_presence_of_pytest_bdd_project():
    pass
