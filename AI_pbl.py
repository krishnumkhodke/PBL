import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia

#robot name = Fury
robot_name = ['fury', 'furi', 'uri', 'curie','theory']
r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()


def listen_for_command():
    print(22)
    with mic as source:
        print('Listening  ...')
        audio = r.listen(source,phrase_time_limit=7)
        print('End')
    try:
        command = r.recognize_google(audio)
        print('You said ',command)
        perform_task(command)
    except:
        engine.say('Sorry I didnt catch that , please try again ')


def perform_task(command):
    command = command.split(' ')
    command = [x.lower() for x in command]
    print(command)

    if command[0] in robot_name:
        if command[1] == 'play':
            video = ' '.join(command[2:])
            engine.say(f'Sure playing {video}')
            pywhatkit.playonyt(video)

        elif command[1] == 'search':
            query = ' '.join(command[2:])
            engine.say('Searching on google ')
            pywhatkit.search(query)

        elif len(command)>3 and (command[1] == 'give' or command[1] == 'gave') and (command[2] == 'info' or command[2] == 'in'):
            query = ' '.join(command[3:])
            try :
                info = wikipedia.summary(query,sentences=3)
                engine.say(info)
                print(info)
            except:
                engine.say('Sorry coudnt find what you were looking for ')
        elif command[1] == 'stop':
                global running
                engine.say('Shutting down ')
                running = False
        else:
            engine.say('Hey how are you doing ')
    else:
        engine.say('hey please Give an valid command ')
        print_current_commands()

def print_current_commands():
    print('1. fury play (video name) ')
    print('2. fury search (search query name)')
    print('3. fury give info (wikipedia topic)')
    print('4. fury stop')

running = True
while running:
    listen_for_command()
    engine.runAndWait()