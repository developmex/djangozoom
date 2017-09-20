import json
from pprint import  pprint
import subprocess
def stado():

    with open('datos.json') as json_data:
        data = json.load(json_data)
        for meetings in data['meetings']:
            lis = data
            for num in lis:
                print(lis)
    return num[0]


contenido = stado()

for n in contenido:

        print n



bashCommand = "./data.sh"
output = subprocess.check_output(['bash','-c', bashCommand])