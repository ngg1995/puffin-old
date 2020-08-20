from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)

from antlr4 import *
from antlr_control import *

class GeneratePuffinFile(Resource):
    def post(self):

        json_data = request.get_json()
        source = json_data['source']

        input = InputStream(source)
        output = antlr_Python3.read(input)

        return {'uncertainties': output}

class Compile(Resource):
    def post(self):

        json_data = request.get_json()
        source = InputStream(json_data['source'])
        uncertainties = InputStream(json_data['uncertainties'])
        language = json_data['language']

        uncerts,changes,dependencies = antlr_puffin.read(uncertainties,language)
        print(changes)
        if language == 'Python3':
            output = antlr_Python3.write(source,uncerts,changes,dependencies)
        elif language == 'R':
            output = antlr_R.write(source,uncerts,changes)
        else:
            raise Exception('Language not known')
        
        return {'output': output}
 
api.add_resource(GeneratePuffinFile, '/GeneratePuffinFile')
api.add_resource(Compile, '/Compile')

if __name__ == '__main__':
    app.run(debug=False)