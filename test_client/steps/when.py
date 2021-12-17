from pytest_bdd import when, parsers


@when(parsers.parse('I search for "{user}" user'))
def i_search_for_user(user):
    """I search for "pytest-dev" user."""
    print(user)


@when(parsers.parse('I select "{project}" project'))
def i_select_project(project):
    """I select "pytest-bdd" project."""
    print(project)
