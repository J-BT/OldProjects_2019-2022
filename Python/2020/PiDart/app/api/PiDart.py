import os, sys
from random import uniform
import pandas as pd
import ctypes
from pathlib import Path
import ast
import json

class Dart:
    """
    [-- Classe of darts --] 
    Attributes : 
        - x = abscissa
        - y = ordinate
        - throws = number of throws

    Class Attributes:
        - numberOfDarts = return the number of dart objects created

    Methods:
        - throw() = throw a dart object
    """
    numberOfDarts = 0

    def __init__(self, abscissa=0, ordinate=0, NumberOfThrows=0):
        self.x = abscissa
        self.y = ordinate
        self.throws = NumberOfThrows
        Dart.numberOfDarts += 1
        print(f"Let's create dart n°{Dart.numberOfDarts}! ")
    
    def throwWithPython(self, maxThrows):
        """
        [Calculating with Python]

        Throws n times darts (until the maximum "maxThrows" be reached).
        Dart's x and y positions are set at random coordinates between -1 and 1.
        
        The method returns 1 json with results :
        {
            "totalThrows": 100000,
            "throwsInside": 78544,
            "throwsOutside": 21456,
            "successRatio": 0.78544,
            "piApproximation": 3.14176
        }

        """
        startTime = pd.Timestamp.now()
        print("And now let's throw it with Python...")
        #throwsCoordinates = {}
        throwsInsideTarget = 0
        throwsOutsideTarget = 0
        

        for throw in range (1, maxThrows + 1):
            xMovement = uniform(-1,1)
            Ymovement= uniform(-1,1)
            self.throws += 1

            self.x = xMovement
            self.y = Ymovement
            # For instance --> throw = 1    
            #                      throwsCoordinates[1] = {"x": 0.9, "y" : -0.27}
            #                  throw = 2 
            #                      throwsCoordinates[2] = {"x": 0.19, "y" : 0.78}
            #                   ...
            #throwsCoordinates[throw] = {"x" : xMovement, "y" : Ymovement}

            if xMovement**2 + Ymovement**2 <= 1:
                throwsInsideTarget += 1

            elif xMovement**2 + Ymovement**2 > 1:
                throwsOutsideTarget += 1
            
            else:
                return f"Throw : {throw} = Something's wrong...This is odd"
            
            # Display each coordinate
            #print(f"New x : {self.x}, new y : {self.y}, throw : {self.throws}")

        successRatio = throwsInsideTarget / self.throws
        piApproximation = successRatio * 4

        #print(f"Total throws : {self.throws}")
        #print(f"Throws inside : {throwsInsideTarget}, Throws outside : {throwsOutsideTarget}")
        #print(f"Succes ratio : {successRatio}, Pi Approximation : {piApproximation}")

        #We create a string 
        throwWithTxt = f"'totalThrows' : {self.throws}, "
        throwWithTxt+= f"'throwsInside' : {throwsInsideTarget}, "
        throwWithTxt+= f"'throwsOutside' : {throwsOutsideTarget}, "
        throwWithTxt+= f"'successRatio' : {successRatio}, "
        throwWithTxt+= f"'piApproximation' : {piApproximation}"
        throwWithTxt = "{"+throwWithTxt+"}"
        # Let's convert it in a dictionnary
        throwWithPyJson = ast.literal_eval(throwWithTxt)
        
        endTime = pd.Timestamp.now()
        
        timeNeeded = (endTime - startTime)

        print(f"Time needed (Python): {timeNeeded}")
        print(f"============================================")

        return throwWithPyJson


    def throwWithC(self, maxThrows):
        """
        [Calculating with C language]

        Throws n times darts (until the maximum "maxThrows" be reached).
        Dart's x and y positions are set at random coordinates between -1 and 1.
        
        The method returns 1 json with results :
        {
            "totalThrows": 100000,
            "throwsInside": 78544,
            "throwsOutside": 21456,
            "successRatio": 0.78544,
            "piApproximation": 3.14176
        }

        """
        startTime = pd.Timestamp.now()
        print("And now let's throw it with C...")
        try:
            soFile = "dataForPythonFile.so"
            cFileImported = ctypes.CDLL(soFile)
            cFileImported.getJsonForPython.argtypes = [ctypes.c_int]
            cFunctionImported = cFileImported.getJsonForPython(maxThrows)
        except:
            #path = os.getcwd()
            #print(path)
            soFile = "app/api/dataForPythonFile.so"
            cFileImported = ctypes.CDLL(soFile)
            cFileImported.getJsonForPython.argtypes = [ctypes.c_int]
            cFunctionImported = cFileImported.getJsonForPython(maxThrows)
        
        #print("-------------Inside jsonToExtractFromC.txt -------------")
        txt = Path('jsonToExtractFromC.txt').read_text()  
        #Adding brackets to dict conversion
        txt = "{"+ txt + "}"
        throwWithcJson = ast.literal_eval(txt)
        #print(throwWithcJson)
    
        

        endTime = pd.Timestamp.now()
        timeNeeded = (endTime - startTime)
        print(f"Time needed (C): {timeNeeded}")
        print(f"============================================")


        return throwWithcJson
    
        
        
###TESTS


GET_PY_JSON = True
GET_C_JSON = True

if __name__ == "__main__":

    if GET_PY_JSON:
        yo = Dart()
        # Bug if > 10 Millions
        PyJson = yo.throwWithPython(500000)    # 10 Millions = 00:00:15.014214
        print("===== P-Json =====")
        print(PyJson)
        print(type(PyJson))

    if GET_C_JSON:
        asobi = Dart()
        # Bug if > 800 Millions
        cJson = asobi.throwWithC(500000)      # 10 Millions = 00:00:01.022130
        print("===== C-Json =====")
        print(cJson)
        print(type(cJson))

    
    print(f"Darts created : {Dart.numberOfDarts}")

   

    
