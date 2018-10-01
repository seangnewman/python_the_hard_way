from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
  # check that a 404 is returned on the / url
  resp = app.request("/")
  assert_response(resp, status="404")

  # test our first GET request to /hello
  resp = app.request("/hello")
  assert_response(resp)

  # make sure default values work for the form
  resp = app.request("/hello", method="POST")
  assert_response(resp,contains="Nobody")

  # test that we get expected values
  data = {'name':'newmanuevers', 'greet' :'Hola'}
  resp = app.request("/hello", method="POST", data=data)
  assert_response(resp, contains="newmanuevers")