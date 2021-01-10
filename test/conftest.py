import os

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture()
def path_test_data(request: FixtureRequest) -> Path:
    return Path(request.fspath).parent.joinpath('data')
