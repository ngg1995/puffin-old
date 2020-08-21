from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)

from antlr4 import *
from antlr_control import *

def generate_puffin_file(source, language):

    input = InputStream(source)

    if language == 'Python3':
        return antlr_Python3.read(input)
    elif language == 'R':
        return antlr_R.read(input)
    else:
        raise Exception('Language not known')

def get_sig_fig(number):

    if '.' in number:
        int_,deci = number.split('.')
        d = -len(deci)
    elif number == '0':
        d = 0
    else:
        zeros = '0'

        while number.endswith(zeros):

            zeros += '0'

        d = len(zeros) - 1


    lower = float(number) - 5*10**(d-1)
    higher = float(number) + 5*10**(d-1)

    return lower,higher

class GeneratePuffinFile(Resource):
    def post(self):

        json_data = request.get_json()
        source = json_data['source']
        language = json_data['language']

        output = generate_puffin_file(source, language) 

        return {'uncertainties': output}

class Compile(Resource):
    def post(self):

        json_data = request.get_json()
        source = InputStream(json_data['source'])
        uncertainties = InputStream(json_data['uncertainties'])
        language = json_data['language']

        uncerts,changes,dependencies = antlr_puffin.read(uncertainties,language)

        if language == 'Python3':
            output = antlr_Python3.write(source,uncerts,changes,dependencies)
        elif language == 'R':
            output = antlr_R.write(source,uncerts,changes)
        else:
            raise Exception('Language not known')
        
        return {'output': output}

class AutoGenerateUncerts(Resource):

    def post(self):
        json_data = request.get_json()
        source = json_data['source']
        uncertainties = json_data['uncertainties']
        language = json_data['language']

        if uncertainties == '':
            uncertainties = generate_puffin_file(source, language)

        auto_uncerts = ''

        for line in uncertainties.split('\n'):

            if '->' in line:

                var, num = line.split('->')

                lower, higher = get_sig_fig(num)
                
                auto_uncerts += '%s-> [%s,%s]\n' %(var,lower, higher)

            else:
                auto_uncerts += line
        
        return {'uncertainties': auto_uncerts}



api.add_resource(GeneratePuffinFile, '/GeneratePuffinFile')
api.add_resource(Compile, '/Compile')
api.add_resource(AutoGenerateUncerts, '/AutoGenerateUncerts')


if __name__ == '__main__':
    app.run(port = 5001, debug=False)