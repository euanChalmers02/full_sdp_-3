# OCR commands to read out full text??
import pyttsx3
from fnd.SoundCode.Buttons.ButtonActions import *

class OCR:

    # should kill in multithreading if state changed using the onword?
    def onWord(self,name, location, length):
        self.word_num = self.word_num + 1
        if check_next_func() is not None:
            action = check_next_func()
            self.engine.stop()
            action()
            print("break @ ", self.word_num)
            self.textToSpeech()
            print("should now resume engine @the last word said & engine should be deid ",self.engine.isBusy())

    def onEnd(self,name, completed):
        self.engine.stop()
        print('finish callback ', name, completed)

    def textToSpeech(self):

        if self.text == "":
            return

        self.engine = pyttsx3.init()
        self.text = self.text.split(" ")
        self.text = self.text[self.word_num:]
        self.text = ' '.join(self.text)
        print("current txt->speech ", self.text)

        self.engine.connect('started-word', self.onWord)
        self.engine.connect('finished-utterance', self.onEnd)

        self.engine.say(self.text)
        self.engine.runAndWait()
        self.engine.stop()

        return True

    def __init__(self, text):
        self.engine = pyttsx3.init()
        self.text = text
        self.word_num = 0

        self.textToSpeech()


