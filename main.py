import speech_recognition as sr
from os import path

flag_dundest = 0

# Initialize recognizer
r = sr.Recognizer()

storage_list = []
storage_set = set()

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "male.wav")

# Open microphone and start recording
with sr.AudioFile(AUDIO_FILE) as source:
#with sr.Microphone() as source:
    print("Listening...")
    while True:
        # Set ambient noise threshold
        r.adjust_for_ambient_noise(source)
        # Capture audio
        audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio, language='en-US')
            text_list = text.split()
            for item in text_list:
                storage_list.append(item)
            print('________________________________________')
            print(f"You said: {text}")
            for word in storage_list:
                storage_set.add(word)

            for word in storage_set:
                print(f'{word}-----{storage_list.count(word)}')

            print('________________________________________')

        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
            flag_dundest +=1
            if flag_dundest >2:
                break


