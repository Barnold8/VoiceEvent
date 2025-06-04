import spacy
import os
import warnings

class similarity:

    # spacy.load()

    def __init__(self,spacyObjectString='en_core_web_sm', similarityThreshold=0.5):

        self.nlp = None
        self.threshold = similarityThreshold
        self.require(spacyObjectString)
    
    def require(self,requireString='en_core_web_sm'):
        warnings.filterwarnings("ignore", category=UserWarning)
        try:
            self.nlp = spacy.load(requireString)
        except Exception as OSError:
            print("Error: could not load required spacy file, downloading now")
            os.system(f"python -m spacy download {requireString}")

    def similarity(self,userInput, instructionSet):

        userInputDocument = self.nlp(userInput)
        test = self.nlp(instructionSet)
        similarity = userInputDocument.similarity(test)
        print(f"Sim: {userInputDocument.similarity(test)} | Threshold: {self.threshold}")
        return userInputDocument.similarity(test) > self.threshold

        

    








