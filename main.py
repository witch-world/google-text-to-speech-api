from gtts import gTTS

audio = gTTS('hello there, I am Google Text-to-Speech API talking to you', lang='en')
audio.save('hello.mp3')