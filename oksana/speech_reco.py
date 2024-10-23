import discord
import speech_recognition as sr
import asyncio
from discord.ext.voice_recv.extras import SpeechRecognitionSink
from typing import Optional
from oksana.oksana import calling_Oksana
from oksana.voice import ReadText

def process_cb(recognizer: sr.Recognizer, audio: sr.AudioData, user:Optional[discord.User]):
    print("Got data")
    text = None
    try:
        text = recognizer.recognize_google(audio,language="zh-tw")
    except sr.UnknownValueError:
        print("Bad speech chunk")
    return text

def text_cb(user, text):
    print(f"{user}:{text}")
    res = calling_Oksana(f"{user}:{text}")

class RecoSink(SpeechRecognitionSink):
    def __init__(self,vc,channel):
        super().__init__()
        self.text_cb = self.text_callback
        self.process_cb = process_cb
        self.phrase_time_limit = 8
        self.vc = vc
        self.channel = channel
    def text_callback(self, user, text):
        vc = self.vc
        channel = self.channel
        if text is None:
            asyncio.run(ReadText(vc,"Error! Tell Koala!"))
            return
        print(f"{user}:{text}")
        res = calling_Oksana(f"{user}:{text}",str(channel.id))
        if res:
            if vc.is_playing():
                vc.stop_playing()
            asyncio.run(ReadText(vc,res))
        else:
            asyncio.run(ReadText(vc,"Error! Tell Koala!"))
    @SpeechRecognitionSink.listener()
    def on_voice_member_speaking_start(self, member):
        #self.vc.stop_playing()
        pass


