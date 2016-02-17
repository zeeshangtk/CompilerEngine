from subprocess import TimeoutExpired
from unittest import TestCase

from compiler_engine.CompilerEngine import CompilerEngine, CompilerException, ProgrammingLanguages


class TestCompile_program(TestCase):
    def test_should_run_code_and_return_the_output(self):
        code = "print(\"hi\")"
        engine = self._create_compiler_engine(code)
        output = engine.compile_program()
        expected_output = bytearray()
        expected_output.extend(b"hi\n")
        self.assertEqual(expected_output, output, "The output is equal")

    def _create_compiler_engine(self, code):
        return CompilerEngine(code, ProgrammingLanguages.PYTHON3)

    def test_should_throw_exception_on_syntax_error(self):
        code = "data s= 10as"
        engine = self._create_compiler_engine(code)
        self.assertRaises(CompilerException,engine.compile_program)

    def test_should_timeout_if_program_run_too_long(self):
        code = "while True: pass"
        engine = self._create_compiler_engine(code)
        self.assertRaises(TimeoutExpired,engine.compile_program)