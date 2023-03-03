import speech_recognition
import pyttsx3 as tts
import sys
import wikipedia as wiki
import webbrowser as wb
import datetime as dt
import googlesearch as GSearch
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)

todo_list =[]

def create_note():
    global recognizer

    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()
    
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                print('listening note....')
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)
                print('recognizing note....')
                note = recognizer.recognize_google(audio,language='en-in')
                note = note.lower()

                with open("notes.txt",'a') as f:
                    f.write(note)
                    f.write("\n")
                    done =True
                    speaker.say("I successfully created the note.")
                    speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()

def add_todo():
    
    global recognizer
    speaker.say("What to do do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                print('Listening your todo ..... ')
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio,language='en-in')
                print('Recognizing your to do....')
                item = item.lower()
                print('Adding {item} to todo list')

                todo_list.append(item)
                done = True
                speaker.say("I added {item} to to do list !")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()

def show_todo():
    speaker.say("Items on your to do list are the following")
    if(len(todo_list)==0):
        speaker.say('Sir ! Your have not added anything to your to do list.')
        speaker.runAndWait()
        return
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def greet():
    speaker.say("Hello ! What can I do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("Closing the application. Bye! See you soon")
    speaker.runAndWait()
    sys.exit(0)

def google_search():
    global recognizer
    speaker.say("What do you want to search on google?")
    speaker.runAndWait()
    done =False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                print('listening search query ......')
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)
                print('recognizing search query ........')
                query = recognizer.recognize_google(audio,language='en-in')
                query = query.lower()
                for j in GSearch.search(query,tld ="co.in",num=5,stop=5,pause=1):
                    wb.open(j)
                done =True
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()
def wiki_search():
    global recognizer
    speaker.say("can you repeat What do you want to know about")
    speaker.runAndWait()
    done =False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                print('listening search query ......')
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)
                print('recognizing search query ........')
                query = recognizer.recognize_google(audio,language='en-in')
                query = query.lower()
                speaker.say("Searching on wikipedia")
                results = wiki.summary(query, sentences=2)
                speaker.say("According to Wikipedia")
                speaker.say(results)
                speaker.runAndWait()
                done=True
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again")
            speaker.runAndWait()


if __name__=="__main__":
    greet()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                print("Listening.....")
                audio = recognizer.listen(mic)
                print("Recognizing.....")
                query = recognizer.recognize_google(audio,language='en-in')
                query.lower()
                print("User Said: ", query,"\n")
                query = query.casefold()

                if 'close'.casefold() in query or 'exit' in query or 'quit' in query or 'leave' in query :
                    quit()
                elif 'to do'.casefold() in query and 'add'.casefold() in query:
                    add_todo()
                elif 'to do'.casefold() in query and ('show'.casefold() in query or 'tell'.casefold() in query ):
                    show_todo()
                elif 'note'.casefold() in query and ('create'.casefold() in query or 'make'.casefold() in query):
                    create_note()
                elif 'open google'.casefold() in query  or 'start Google'.casefold() in query:
                    wb.open("google.com")
                elif 'open youtube'.casefold() in query or 'start youtube'.casefold() in query:
                    wb.open("youtube.com")
                elif ('tell'.casefold() in query or 'what'.casefold() in query) and 'time'.casefold() in query:
                    strTime = dt.datetime.now().strftime("%H:%M:%S")    
                    speaker.say(f"Sir, the time is {strTime}")
                    speaker.runAndWait()
                elif ('tell'.casefold() in query or 'what'.casefold() in query) and 'date'.casefold() in query:
                    strTime = dt.datetime.now().strftime("%d:%B:%Y")    
                    speaker.say(f"Sir, the date is {strTime}")
                    speaker.runAndWait()
                elif ('search'.casefold() in query or 'find'.casefold() in query) and ('google'.casefold() in query or 'browser'.casefold() in query):
                    google_search()
                elif 'what is'.casefold() in query or 'who is'.casefold() in query or 'wikipedia'.casefold() in query:
                    wiki_search()
                elif 'hello'.casefold() in query or 'hi'.casefold() in query or 'how are you'.casefold() in query or 'whats up'.casefold() in query or 'are you there'.casefold() in query:
                    greet()
                else:
                    speaker.say('Sorry Sir! These are beyond my Limitations.')
                    speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()


