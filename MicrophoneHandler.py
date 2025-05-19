import speech_recognition as sr

r=sr.Recognizer()

class MicHandler:

    def __init__(self):

        self.m_micIndex = MicHandler.getMicrophoneIndex()

    def displayMicrophones():
        integer = 0

        for mic in sr.Microphone.list_microphone_names():
            print(f"{integer}. {mic}")
            integer += 1

    def getMicrophoneIndex():
        
        MicHandler.displayMicrophones()

        try:
            mic_index = int(input("Pick a number: "))
        except ValueError as vE:
            print(f"FATAL ERROR: {vE}")
            return -1
        
        return mic_index

    def getPhrase(self):

        with sr.Microphone(device_index=self.m_micIndex) as source:

            r.adjust_for_ambient_noise(source, duration=5)
            print("say anything : ")
            audio = r.listen(source)
            try:
                text = r.recognize_sphinx(audio)
                print(text)
            except:
                print("sorry, could not recognise")