# Obiezue Ifechukwu
# 2019234067
# Electrical Engineering 
# ECE 331
# Signal and Systems 
# Speech to Text Recognition Project

# Import the library in your Python script
import speech_recognition as sr

# Initialize a recognizer object:
r = sr.Recognizer()

# Use the Microphone class to access the microphone and record audio:
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something...\nTry Saying\nHey Siri!")
    audio = r.listen(source)

# Use the recognize_google() method to perform speech recognition
siriSpeechRecognitionSystem = r.recognize_google(audio)
print("You said: " + siriSpeechRecognitionSystem)

# Add error handling to handle cases where the speech recognition fails
try:
    siriSpeechRecognitionSystem = r.recognize_google(audio)
    print("You said: " + siriSpeechRecognitionSystem)
except sr.UnknownValueError:
    print("Apple Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Apple Speech Recognition service; {0}".format(e))

