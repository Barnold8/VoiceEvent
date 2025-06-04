# VoiceEvent

A python program to attach events to user speech

# How to install

1. clone the repo
2. Run ``pip install -r requirements.txt`` in the root directory of cloned project (use a venv if you dont want to install the libraries system wide)
3. Run python main.py and enjoy

# Configs

## Settings

This is how you will configure how the program works generally

Here is the file in its most default state

```json
{
    "Calibration":{
        "use": true,
        "autoCalibrate": false,
        "duration": 1,
        "energyThreshold": 50,
        "dynamicEnergyThreshold": false
    },

    "SaveFile":{
        "use": true,
        "location": "./Data"
    },

    "Model":{
        "use":true,
        "modelName": "en_core_web_sm",
        "threshold": 0.7
    }

}
```
And here is the file explained

### Calibration

When using the app, you will need to calibrate your microphone, so here's how this section works.

| Name    | Usage |
| -------- | ------- |
| use  | if the custom setting is used    |
| autoCalibrate | if the energy threshold is automatically handled given by listening to your microphone     |
| duration    | how long to listen for automatic calibration    |
| energyThreshold    |   how sensitive the microphone will be to audio, the higher the number, the less sensitive it will be (a higher number is better if you have more ambient noise)  |
| dynamicEnergyThreshold    | automatically assume energyThreshold    |


### SaveFile

This is just a simple text file that keeps memory of the microphone you have selected previously

| Name    | Usage |
| -------- | ------- |
| use  | if the custom setting is used    |
| location | where the custom save file is located on disk    |

### Model

| Name    | Usage |
| -------- | ------- |
| use  | if the custom setting is used    |
| modelName | what model is used for similarity matching  |
| threshold | how accurate the user's speech has to be to a given command phrase [between 0.0-1.0] lower means less accurate  |
