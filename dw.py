from pytube import YouTube 

yt = YouTube("https://www.youtube.com/watch?v=K0e8gxJ5JbI").streams.first()
yt.streams.download()