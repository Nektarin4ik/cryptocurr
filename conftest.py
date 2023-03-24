import pytest
from pytest_django.plugin import pytest_configure

pytest_configure()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


