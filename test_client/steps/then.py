from pytest_bdd import then


@then('I should see the repository page')
def i_should_see_the_repository_page():
    """I should see the repository page."""
    print('On page')
