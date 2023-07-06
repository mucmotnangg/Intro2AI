import os
from mySolution import *

DIR = os.path.dirname(os.path.abspath(__file__))
INPUT=DIR+'\INPUT'
OUTPUT=DIR+'\OUTPUT'

def main():
    for file in os.listdir(INPUT):
        ms=MySolution()
        ms.getInput(os.path.join(os.path.dirname(__file__),r'INPUT/'+file))
        ms.PLSolution()
        file_output = "output"+file[file.find('input')+5:]
        ms.writeOutput(os.path.join(os.path.dirname(__file__),r'OUTPUT/'+file_output))


if __name__ == '__main__':
    main()