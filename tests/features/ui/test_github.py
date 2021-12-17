from pytest_bdd import scenario


@scenario('github.feature', 'Verify presence of pytest-bdd project')
def test_verify_presence_of_pytest_bdd_project():
    """Verify presence of pytest-bdd project."""
