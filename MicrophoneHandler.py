import speech_recognition as sr

class MicHandler:

    def __init__(self,saveLocation=None,calibrationDuration=None):

        self.recognizer = sr.Recognizer()
        
        loaded_microphone = self.LoadMicrophone()

        if loaded_microphone != -1:
            self.micIndex,self.micName = loaded_microphone
        else:
            self.micIndex,self.micName = MicHandler.GetMicrophoneInformation()

        self.microphone = sr.Microphone(device_index=self.micIndex)
        
        self.recognizer.adjust_for_ambient_noise(self.microphone) 

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

    def GetPhrase(self):

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(source, duration=5)
            print("Listening: ")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_sphinx(audio)
                print(text)
            except:
                print("sorry, could not recognise")

    def SaveMicrophone(self):
        with open("Data/MicrophoneSave.micSave","w") as saveFile:
            saveFile.write(f"Mic: {self.m_micName}")

    def LoadMicrophone(self):

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
                
        except FileNotFoundError as fileNotFoundErr:
            return -1
        
    def CalibrateNoiseAdjustment(self,duration):
        print(f"Calibrating for ambient noise. Please wait {duration} seconds...")
        self.recognizer.adjust_for_ambient_noise(self.microphone,duration)