import pytest
import os
from predict.app import create_app


@pytest.fixture
def app():
    os.chdir(os.getcwd().replace("tests", "app"))
    app = create_app()
    return app

