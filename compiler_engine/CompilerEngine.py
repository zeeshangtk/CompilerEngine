import logging
import os
import random
from enum import Enum
from subprocess import Popen, PIPE

BASE_DIR = "/tmp/"
TIMEOUT_IN_SEC = 5


class CompilerEngine:

    def __init__(self, code, program_type):
        self.code = code
        self.program_type = program_type

    def compile_program(self):
        file = None
        try:
            file = self._create_program_file()
            return self._execute_program_file(file)
        except CompilerException as e:
            logging.error("Error while executing the code " + self.code + "ERROR " + str(e))
            raise e
        finally:
            os.remove(file)

    def _create_program_file(self):
        random_file = BASE_DIR + str(random.random()) +"."+ self.program_type.get_extension_type()
        logging.info("The file path is " + random_file)
        with  open(random_file, 'w') as file_obj:
            file_obj.write(self.code)
        return random_file

    def _execute_program_file(self, file_path):
        # command = "/Applications/Racket\ v6.3/bin/racket "+file_path
        command = self.program_type.get_compilation_command()+" " + file_path
        process = None
        try:
            process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        except Exception as e:
            raise CompilerException(e)
        stdout, stderr = process.communicate(timeout=TIMEOUT_IN_SEC)
        logging.info("The output is " + str(stdout))
        if stderr != bytearray():
            logging.error("Got error " + str(stderr))
            raise CompilerException("Error: " + str(stderr))
        return stdout


class CompilerException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class ProgrammingLanguages(Enum):
    PYTHON3 = ("python3", "py")
    PYTHON = ("python", "py")
    RACKET = ("racket", "rkt")

    def get_compilation_command(self):
        return self.value[0]

    def get_extension_type(self):
        return self.value[1]

    @staticmethod
    def get_programming_language(programming_lang):
        programming_lang = programming_lang.lower()
        for e in ProgrammingLanguages:
            if programming_lang == "python3":
                return ProgrammingLanguages.PYTHON3

            if programming_lang == "python":
                return ProgrammingLanguages.PYTHON

            if programming_lang == "racket":
                return ProgrammingLanguages.RACKET


if __name__=="__main__":
     data = ProgrammingLanguages.get_programming_language("python")
     print(data)