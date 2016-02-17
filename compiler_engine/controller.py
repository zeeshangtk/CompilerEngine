#!flask/bin/python
import logging
from os import abort

from flask import Flask
from flask import request

from compiler_engine.CompilerEngine import CompilerEngine, ProgrammingLanguages

application = Flask(__name__)


@application.route('/compile',methods=["POST"])
def compile_code():

    if not request.json:
        abort(400)

    code = request.json["code"]
    program_type = ProgrammingLanguages.get_programming_language(str(request.json["type"]))
    logging.info("The code to be excuted is "+code)
    return CompilerEngine(code,program_type).compile_program()

if __name__ == '__main__':
    application.run(debug=True)
