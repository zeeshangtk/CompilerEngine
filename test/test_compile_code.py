import unittest
from unittest import TestCase

from flask import json

from compiler_engine import controller
from compiler_engine.CompilerEngine import ProgrammingLanguages


class TestController(TestCase):

    def setUp(self):
        self.app = controller.application.test_client()

    def test_should_return_the_output(self):
        output = self._call_compile_rest_api("print('hi')",ProgrammingLanguages.PYTHON3.value)
        for i in output:
            self.assertEqual(i,b"hi\n")

    def _call_compile_rest_api(self, code,type):
        input_json_data = json.dumps(dict(code=code,type=type))
        response = self.app.post("/compile",
                                 data=input_json_data,
                                 content_type='application/json')
        return response.response


if __name__=="main":
    unittest.main()