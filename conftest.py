import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\python\\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
