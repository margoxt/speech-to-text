import speech_recognition as sr             #This makes the program listen to audio from mic or file & converts speech into text
import pyttsx3                              #This makes the program speak text out loud.


#Initialize the recognizer. This is the object that is used to interact with the microphone
r = sr.Recognizer()

#Step 1: Allow the computer's microphone to listen for audio input and turn it into a string
def record_text():
    # Loop in case of errors (unidentifiable audio)
    while True: 
        try:
            #Use the microphone as a source of input
            with sr.Microphone() as audio_source:    

                #Prepare recognizer to receive input
                r.adjust_for_ambient_noise(audio_source, duration=0.2)

                #Use the recognizer's listen function
                captured_audio = r.listen(audio_source)

                #The audio2 will be then used by the recognize_google function to recognize the spoken words and make it string
                recog_text = r.recognize_google(captured_audio)

                return recog_text

        except sr.RequestError as error:
            print(f"Could not request results; {error}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")


#Step 2: Take the string from step 1 and output it as a text file
def output_text(speech_text):

    # Open a text file using the open function, this will allow us to access the output.txt file in the directory of the program. If there's no file, the program will create one automatically
    with open("output.txt", "a") as f:              #with open(...) as f, python creates a context manager.
        f.write(speech_text + "\n")
    return speech_text

#Step 3: The while loop calls the two functions on repeat
print("Listening...")

while(True):
    speech_text = record_text()
    if speech_text:     #Only print if we got valid text
        print(output_text(speech_text))
