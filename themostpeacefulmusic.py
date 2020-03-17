from __future__ import unicode_literals
import youtube_dl
from moviepy.editor import *
import os
import random


videolink=input('enter yt link: ').replace('"','').replace("'",'')
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([videolink])
    vidinfo = ydl.extract_info(videolink, download=False)
    vidid = vidinfo.get("id", None)
    vidtitle = vidinfo.get('title', None)


music=vidtitle.replace(':',' -').replace('/','_')+'-'+vidid+'.webm'

musicclip = VideoFileClip(music)
durationofmusiciclip=musicclip.duration
rain = AudioFileClip('Support\\Rain.mp3')
rain = afx.audio_loop(rain, duration=durationofmusiciclip)
rainclip = VideoFileClip('Support\\'+random.choice(['1','2','3','4'])+'.gif').loop(duration= durationofmusiciclip).resize((1920,1080))

new_videoclip = CompositeVideoClip([musicclip, rainclip])
new_audioclip = CompositeAudioClip([musicclip.audio, rain])
musicclip.audio = new_audioclip
new_videoclip = new_videoclip.set_audio(musicclip.audio)
new_videoclip.write_videofile(vidtitle.replace(':',' -').replace('/','_')+' - Rain.mp4')

os.remove(music)


