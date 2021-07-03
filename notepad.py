import tkinter as tk
from tkinter import *
import speech_recognition as sr
import time
from time import ctime
import os

root = tk.Tk()
root.title('Voice Notepad')
root.resizable(width=False, height=False)
frame_button = Frame(root, bg = 'gray')
frame_button.pack(side = LEFT, fill=BOTH)
frame_textarea = Frame(root, bg = 'gray')
frame_textarea.pack(side = LEFT, fill=BOTH)
TextArea = Text(frame_textarea, height=21, width=50)
TextArea.pack(padx=20, pady=20)

def clearScreen():
    TextArea.delete('1.0', END)

def convertSpeechToText():
    r = sr.Recognizer()


    with sr.Microphone(device_index=2) as source:
        print("Adjusting noise ")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Recording")
        recorded_audio = r.listen(source)
        print("Done recording")
        data = ''
        insert_data = ''
        try:
            print("Recognizing the text")
            data = r.recognize_google(recorded_audio)
            insert_data = insert_data + ' ' + data
            TextArea.insert(INSERT, insert_data)
            print("Decoded Text : {}".format(insert_data))
        
        except sr.UnknownValueError:
                insert_data='Google Speech Recognition could not understand audio';
                TextArea.insert(INSERT, insert_data)
        except sr.RequestError as e:
                insert_data='Could not request results from Google Speech Recognition service; {0}'.format(e)
                TextArea.insert(INSERT, insert_data)


def writeToFile():
    speech_data=TextArea.get(1.0,END)
    save_path = os.getcwd()
    name_of_file = getFileName()
    completeName = os.path.join(save_path, name_of_file+'.txt')
    file1 = open(completeName, 'w')
    file1.write(speech_data)
    file1.close()

def getFileName():
    ts = time.time()
    ts=int(ts)
    ts=str(ts)
    return ts

btn_export = Button(frame_button, text='Export', compound='top',command=writeToFile, height=10, width=10)
btn_export.pack(pady = 5, padx = 5)
btn_speak = Button(frame_button, text='Speak', compound='top',command=convertSpeechToText, height=10, width=10)
btn_speak.pack(pady = 5, padx = 5)
btn_reset = Button(frame_button, text='Reset', compound='top',command=clearScreen, height=10, width=10)
btn_reset.pack(pady = 5, padx = 5)
root.mainloop()