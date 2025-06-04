from MicrophoneHandler import *
from WordSimilarity import *
from Command import *

# Add NLTK for similarity matching for given actions defined in Commands.json
# Add settings parsing for loading microphone object
# Make wrapper class for keyboard commands to pynput keyboard pressing functions

def main():

    running = True

    if __name__ == "__main__":

        micHandler = MicrophoneHandler.initMicrophone()
        micHandler.SaveMicrophone()

        keys = KeyCommand()

        similarityMatcher = similarity()

        while running:

            if similarityMatcher.similarity(micHandler.GetPhrase(),"big boss"):
                keys.keyPress(["f12"])


            


main()


        # keyboard = Controller()

        # keyboard.press(Key.f12)
        # keyboard.release(Key.f12)