import speech_recognition as sr
import json

class MicrophoneHandler:

    def __init__(self,saveLocation=None,calibrationDuration=None):

        self.recognizer = sr.Recognizer()
        self.micName = None 
        self.micIndex = None
        loaded_microphone = self.LoadMicrophone()

        if loaded_microphone != -1:
            self.micIndex,self.micName = loaded_microphone
        else:
            self.micIndex,self.micName = MicrophoneHandler.GetMicrophoneInformation()

        self.microphone = sr.Microphone(device_index=self.micIndex)
        
        if calibrationDuration:
            self.CalibrateNoiseAdjustment(calibrationDuration)

    def GetMicrophoneInformation():

        integer = 0
        microphones = sr.Microphone.list_microphone_names()

        for mic in microphones:
            print(f"{integer}. {mic}")
            integer += 1

        try:
            mic_index = int(input("Pick a number: "))
        except ValueError as vE:
            print(f"FATAL ERROR: {vE}")
            return -1
        
        return [mic_index,microphones[mic_index]]

    def GetPhrase(self,saveLocation=None):

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(source, duration=5)
            print("Listening: ")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_sphinx(audio)
                print(text)
                return text
            except:
                print("sorry, could not recognise")
                return "N/A"

    def SaveMicrophone(self):
        with open("Data/MicrophoneSave.micSave","w") as saveFile:
            saveFile.write(f"Mic: {self.micName}")

    def LoadMicrophone(self,loadLocation=None):

        try:
            with open("Data/MicrophoneSave.micSave","r") as file:
                
                file_contents = file.read()
                
                if len(file_contents) > 0:

                    if ":" not in file_contents:
                        print("Error: Expected : char in .micSave file but found none")
                        return -1
                    else:
                        parsed_contents = file_contents.split(":")[1].strip()
                        microphones = sr.Microphone.list_microphone_names()
                        possible = [mic for mic in microphones if parsed_contents in mic or parsed_contents == mic] # grabs every microphone that matches the save file
                
                        if len(possible) > 0:
                            return [microphones.index(possible[0]),possible[0]]
                        else:
                            return -1
                else:
                    return -1
                
        except FileNotFoundError as fileNotFoundErr:
            return -1
        
    def CalibrateNoiseAdjustment(self,autoCalibrate=False,duration=1,energyThreshold=50,dyamicEnergyThreshold=False):
        grammar = "seconds" if duration > 1 else "second"

        if autoCalibrate:
            print(f"Calibrating for ambient noise. Please wait {duration} {grammar}...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(self.microphone,duration)
        else:
            self.recognizer.energy_threshold = energyThreshold
            self.recognizer.dynamic_energy_threshold = dyamicEnergyThreshold

    def initMicrophone():
        try:
            with open("Data/settings.json","r") as file:
                try:
                    settings = json.load(file)
                    useDuration = 1 if settings["Calibration"]["use"] == True else 0
                    useSaveLocation = settings["SaveFile"]["location"] if settings["SaveFile"]["use"] == True else None

                    return MicrophoneHandler(
                        saveLocation        = useSaveLocation,
                        calibrationDuration = settings["Calibration"]["duration"]*useDuration
                    )
                
                except KeyError as keyErr:
                    print(f"Error: Problem accessing data in Settings.json, returning default microphone handler\nErrorINFO: {keyErr}")
                    return MicrophoneHandler()
            
        except FileNotFoundError as fileErr:
            print("Error: Could not find Settings.json, make sure it is in the relative Data directory. Skipping the settings load sequence, this may lead to undefined program behaviour")
            return MicrophoneHandler()
    