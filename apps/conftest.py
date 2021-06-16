import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):# noqa
    settings.MEDIA_ROOT = tmpdir.strpath
