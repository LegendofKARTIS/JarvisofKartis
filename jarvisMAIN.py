import sys
import random, pywhatkit, pyttsx3, datetime, sys, time, os, pyautogui, requests, wikipedia, pyjokes
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from jarvisMainGUI import Ui_JarvisMainGUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishings():
    ui.updateMovieDynamically("speaking")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrint("Jarvis: Good Morning BOSS")
        speak("Good Morning BOSS")
    elif hour >= 12 and hour < 17:
        ui.terminalPrint("Jarvis: Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour >= 17 and hour < 21:
        ui.terminalPrint("Jarvis: Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        ui.terminalPrint("Jarvis: Good Night BOSS")
        speak("Good Night BOSS")


class jarvisMainClass(QThread):
    def __init__(self):
        super(jarvisMainClass, self).__init__()

    def run(self):
        self.runJarvis()

    def commands(self):
        ui.updateMovieDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            ui.updateMovieDynamically("loading")
            ui.terminalPrint("Wait for few Moments..")
            cmd = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {cmd}\n")
    
        except Exception as e:
            ui.terminalPrint(e)
            speak("Please tell me again")
            cmd = "none"
        return cmd
    
    def runJarvis(self):
        wishings()
        while True:
            self.query = self.commands().lower()
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open firefox' in self.query:
                speak("Opening Firefox Application sir...")
                os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

            elif "wikipedia" in self.query:
                speak("Searching in Wikipedia")
                try:
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=1)
                    speak("According to Wikipedia,")
                    ui.terminalPrint(results)
                    speak(results)
                except:
                    speak("No Results found Sir...")
                    ui.terminalPrint("No results Found")

            elif 'play' in self.query:
                self.query = self.query.replace('play', '')
                speak('Playing' + self.query)
                pywhatkit.playonyt(self.query)

            elif 'type' in self.query:
                speak("Please tell me what should i write")
                while True:
                    writeInNotepad = self.commands()
                    if writeInNotepad == 'exit typing':
                        speak("Done sir")
                    else:
                        pyautogui.write(writeInNotepad)

            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                ui.terminalPrint(joke)
                speak(joke)

            elif 'exit program' in self.query:
                speak("I'm Leaving Sir, BYE!")
                quit()


startExecution = jarvisMainClass()


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.jarvisUI = Ui_JarvisMainGUI()
        self.jarvisUI.setupUi(self)

        self.jarvisUI.exitButton.clicked.connect(self.close)
        self.jarvisUI.enterButton.clicked.connect(self.manualCodeFromTerminal)
        self.runAllMovies()

    def manualCodeFromTerminal(self):
        if self.jarvisUI.terminalInputBox.text():
            cmd = self.jarvisUI.terminalInputBox.text()
            self.jarvisUI.terminalInputBox.clear()
            self.jarvisUI.terminalOutputBox.appendPlainText(f"You typed-> {cmd}")

            if cmd == 'exit':
                ui.close()
            elif cmd == 'help':
                self.terminalPrint("I can perform various tasks which is programmed inside me by KARTIS sir.\n"
                                   "Examples are: Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")

            else:
                pass

    def terminalPrint(self, text):
        self.jarvisUI.terminalOutputBox.appendPlainText(text)

    def updateMovieDynamically(self, state):
        if state == "speaking":
            self.jarvisUI.jarvisSpeakingLabel.raise_()
            self.jarvisUI.jarvisSpeakingLabel.show()
            self.jarvisUI.listeningLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        elif state == "listening":
            self.jarvisUI.listeningLabel.raise_()
            self.jarvisUI.listeningLabel.show()
            self.jarvisUI.jarvisSpeakingLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        elif state == "loading":
            self.jarvisUI.loadingLabel.raise_()
            self.jarvisUI.loadingLabel.show()
            self.jarvisUI.jarvisSpeakingLabel.hide()
            self.jarvisUI.listeningLabel.hide()

    def runAllMovies(self):
        self.jarvisUI.codingMovie = QtGui.QMovie("E:\\CODING\\Artificial_Intelligence\\Ultimate JARVIS with GUI YT  Playlist files\\gui_tools\\B.G_Template_1.gif")
        self.jarvisUI.codingLabel.setMovie(self.jarvisUI.codingMovie)
        self.jarvisUI.codingMovie.start()

        self.jarvisUI.listeningMovie = QtGui.QMovie(
            "E:\\CODING\\Artificial_Intelligence\\Jarvis with GUI\\gui_tools\\listening.gif")
        self.jarvisUI.listeningLabel.setMovie(self.jarvisUI.listeningMovie)
        self.jarvisUI.listeningMovie.start()

        self.jarvisUI.speakingMovie = QtGui.QMovie(
            "E:\\CODING\\Artificial_Intelligence\\Jarvis with GUI\\gui_tools\\speaking.gif")
        self.jarvisUI.jarvisSpeakingLabel.setMovie(self.jarvisUI.speakingMovie)
        self.jarvisUI.speakingMovie.start()

        self.jarvisUI.arcMovie = QtGui.QMovie(
            "E:\\CODING\\Artificial_Intelligence\\Jarvis with GUI\\gui_tools\\techcircle.gif")
        self.jarvisUI.arcLabel.setMovie(self.jarvisUI.arcMovie)
        self.jarvisUI.arcMovie.start()

        self.jarvisUI.loadingMovie = QtGui.QMovie(
            "E:\\CODING\\Artificial_Intelligence\\Jarvis with GUI\\gui_tools\\tech loading-cropped.gif")
        self.jarvisUI.loadingLabel.setMovie(self.jarvisUI.loadingMovie)
        self.jarvisUI.loadingMovie.start()

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()
    sys.exit(app.exec_())
