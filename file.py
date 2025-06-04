import json
from Command import *


def loadSettings(filePath:str):
    pass

def loadCommands(filePath:str) -> list:

    # load every command type listed in Commands.json that is ALSO supported
    commandObjects = []
    commandTypes = {
        "keycommands": KeyCommand
    }

    with open(filePath) as file:
        file_contents = file.read()
        contents = json.loads(file_contents)

        commandTypeKeys = list(commandTypes.keys())
        commandFileKeys = list(contents.keys())

        for key in commandFileKeys:
            if key.lower() in commandTypeKeys:
                # append supported object via a reference to its class in commandTypes and provide it with data binding found within Commands.json
                commandObjects.append(commandTypes[key.lower()](contents[key]))

    return commandObjects