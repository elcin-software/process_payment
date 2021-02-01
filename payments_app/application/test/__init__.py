# -*- coding: utf-8 -*-

import pytest
from webtest import TestApp

from application.app import createApp



@pytest.fixture
def app():
    _app = createApp("test.settings")
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture
def testapp(app):
    return TestApp(app)