from MicrophoneHandler import *
from Command import *
from file import *

# Add NLTK for similarity matching for given actions defined in Commands.json
# Add settings parsing for loading microphone object

def main():

    running = True

    if __name__ == "__main__":

        micHandler = MicrophoneHandler.initMicrophone()
        micHandler.SaveMicrophone()

        commandObjects = loadCommands("Data/Commands.json")

        similarityMatcher = Similarity()

        while running:

            userSpeech = micHandler.GetPhrase()

            for object in commandObjects:
                object.action(userSpeech,similarityMatcher)

main()
