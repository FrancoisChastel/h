# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
"""
The `conftest` module is automatically loaded by py.test and serves as a place
to put fixture functions that are useful application-wide.
"""

import functools
import os

import deform
import mock
import pytest

import click.testing
import sqlalchemy
from pyramid import testing
from pyramid.request import apply_request_extensions
from sqlalchemy.orm import sessionmaker
from webob.multidict import MultiDict

from h import db
from h.settings import database_url
from h._compat import text_type
from h import accounts
from h import schemas
from h import search    #PROPER IMPORT for search module

TEST_AUTHORITY = u'example.com'
TEST_DATABASE_URL = database_url(os.environ.get('TEST_DATABASE_URL',
                                                'postgresql://postgres@localhost/htest'))

Session = sessionmaker()


class DummyFeature(object):

    """
    A dummy feature flag looker-upper.

    Because we're probably testing all feature-flagged functionality, this
    feature client defaults every flag to *True*, which is the exact opposite
    of what happens outside of testing.
    """

    def __init__(self):
        self.flags = {}
        self.loaded = False

    def __call__(self, name, *args, **kwargs):
        return self.flags.get(name, True)

    def all(self):
        return self.flags

    def load(self):
        self.loaded = True

    def clear(self):
        self.flags = {}


class DummySession(object):

    """
    A dummy database session.
    """

    def __init__(self):
        self.added = []
        self.deleted = []
        self.flushed = False

    def add(self, obj):
        self.added.append(obj)

    def delete(self, obj):
        self.deleted.append(obj)

    def flush(self):
        self.flushed = True


# A fake version of colander.Invalid
class FakeInvalid(object):
    def __init__(self, errors):
        self.errors = errors

    def asdict(self):
        return self.errors


def autopatcher(request, target, **kwargs):
    """Patch and cleanup automatically. Wraps :py:func:`mock.patch`."""
    options = {'autospec': True}
    options.update(kwargs)
    patcher = mock.patch(target, **options)
    obj = patcher.start()
    request.addfinalizer(patcher.stop)
    return obj


@pytest.yield_fixture
def cli():
    runner = click.testing.CliRunner()
    with runner.isolated_filesystem():
        yield runner


@pytest.fixture(scope='session')
def db_engine():
    """Set up the database connection and create tables."""
    engine = sqlalchemy.create_engine(TEST_DATABASE_URL)
    db.init(engine, should_create=True, should_drop=True, authority=TEST_AUTHORITY)
    return engine


@pytest.yield_fixture
def db_session(db_engine):
    """
    Prepare the SQLAlchemy session object.

    We enable fast repeatable database tests by setting up the database only
    once per session (see :func:`db_engine`) and then wrapping each test
    function in a transaction that is rolled back.

    Additionally, we set a SAVEPOINT before entering the test, and if we
    detect that the test has committed (i.e. released the savepoint) we
    immediately open another. This has the effect of preventing test code from
    committing the outer transaction.
    """
    conn = db_engine.connect()
    trans = conn.begin()
    session = Session(bind=conn)
    session.begin_nested()

    @sqlalchemy.event.listens_for(session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.begin_nested()

    try:
        yield session
    finally:
        session.close()
        trans.rollback()
        conn.close()


@pytest.yield_fixture
def factories(db_session):
    from ..common import factories
    factories.set_session(db_session)
    yield factories
    factories.set_session(None)


@pytest.fixture
def fake_feature():
    return DummyFeature()


@pytest.fixture
def fake_db_session():
    return DummySession()


@pytest.fixture
def form_validating_to():
    def form_validating_to(appstruct):
        form = mock.MagicMock()
        form.validate.return_value = appstruct
        form.render.return_value = 'valid form'
        return form
    return form_validating_to


@pytest.fixture
def invalid_form():
    def invalid_form(errors=None):
        if errors is None:
            errors = {}
        invalid = FakeInvalid(errors)
        form = mock.MagicMock()
        form.validate.side_effect = deform.ValidationFailure(None, None, invalid)
        form.render.return_value = 'invalid form'
        return form
    return invalid_form


@pytest.fixture
def mailer(pyramid_config):
    from pyramid_mailer.interfaces import IMailer
    from pyramid_mailer.testing import DummyMailer
    mailer = DummyMailer()
    pyramid_config.registry.registerUtility(mailer, IMailer)
    return mailer


@pytest.fixture
def matchers():
    from ..common import matchers
    return matchers


@pytest.fixture
def notify(pyramid_config, request):
    patcher = mock.patch.object(pyramid_config.registry, 'notify', autospec=True)
    request.addfinalizer(patcher.stop)
    return patcher.start()


@pytest.fixture
def patch(request):
    return functools.partial(autopatcher, request)


@pytest.yield_fixture
def pyramid_config(pyramid_settings, pyramid_request):
    """Pyramid configurator object."""
    with testing.testConfig(request=pyramid_request,
                            settings=pyramid_settings) as config:
        # Include pyramid_services so it's easy to set up fake services in tests
        config.include('pyramid_services')
        apply_request_extensions(pyramid_request)

        yield config


@pytest.fixture
def pyramid_request(db_session, fake_feature, pyramid_settings):
    """Dummy Pyramid request object."""
    request = testing.DummyRequest(db=db_session, feature=fake_feature)
    request.authority = text_type(TEST_AUTHORITY)
    request.create_form = mock.Mock()
    request.matched_route = mock.Mock()
    request.registry.settings = pyramid_settings
    request.is_xhr = False
    request.params = MultiDict()
    request.GET = request.params
    request.POST = request.params
    return request


@pytest.fixture
def pyramid_csrf_request(pyramid_request):
    """Dummy Pyramid request object with a valid CSRF token."""
    pyramid_request.headers['X-CSRF-Token'] = pyramid_request.session.get_csrf_token()
    return pyramid_request


@pytest.fixture
def pyramid_settings():
    """Default app settings."""
    return {
        'sqlalchemy.url': TEST_DATABASE_URL
    }

@pytest.fixture(autouse=True)
def coverageFix():
    result = [[0.,0.],[0.,0.],[0.,0.],[0.,0.],[0.,0.]]      #result data structure

    #create loop for the module, counting the trues in the data structure MUST IMPORT PROPER FILE
    #must create data strcuture in each file

    for element in search.client.branches:  #search/client.py (branches is data structure)
        if element == True:
            result[0][0] += 1.
        result[0][1] += 1.

    for element in search.parser.branches:  #search/parser.py
        if element == True:
            result[1][0] += 1.
        result[1][1] += 1.

    for element in search.index.branches:   #search/index.py
        if element == True:
            result[2][0] += 1.
        result[2][1] += 1.

    for element in search.query.branches:   #search/query.py
        if element == True:
            result[3][0] += 1.
        result[3][1] += 1.

    for element in accounts.schemas.branches: #accounts/schemas.py
        if element == True:
            result[4][0] += 1.
        result[4][1] += 1.

    trues = 0.
    falses = 0.

    for element in result:                  #count all trues and total branches
        trues += element[0]
        falses += element[1]

    falses = (trues/falses)*100

    print('===============================================')
    print('Test coverage for client.py is {0}%'.format(int((result[0][0]/result[0][1])*100)))
    print('Test coverage for parser.py is {0}%'.format(int((result[1][0]/result[1][1])*100)))
    print('Test coverage for index.py is {0}%'.format(int((result[2][0]/result[2][1])*100)))
    print('Test coverage for query.py is {0}%'.format(int((result[3][0]/result[3][1])*100)))
    print('Test coverage for schemas.py is {0}%'.format(int((result[4][0]/result[4][1])*100)))

    print('Total test coverage is {0}%'.format(int(falses)))
    
