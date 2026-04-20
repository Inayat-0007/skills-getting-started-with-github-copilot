from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

INITIAL_ACTIVITIES = deepcopy(app_module.activities)


def _reset_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    _reset_activities()
    yield
    _reset_activities()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
