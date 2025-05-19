from MicrophoneHandler import *

# Add NLTK for similarity matching for given actions defined in Commands.json
# Implement settings.json for actually deciding logic at runtime



def main():

    running = True

    if __name__ == "__main__":

        micHandler = MicrophoneHandler.initMicrophone()
        micHandler.SaveMicrophone()

        while running:
            micHandler.GetPhrase()


main()