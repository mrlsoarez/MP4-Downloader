from pytube import YouTube

class Video():
    def __init__(self, title, thumb, link):
        self.title = title 
        self.thumb = thumb
        self.link = link

# atributos que consigo acessar:
        
    # title 
    # thumbnail_url
def getYoutubeVideo():
    try:
        link = YouTube('https://www.youtube.com/watch?v=WcCGpUc1yrI')
        return Video(link.title, link.thumbnail_url, link)
    except:
        print('O link do youtube não está funcionando corretamente!')

video = getYoutubeVideo()
print(video.title, video.thumb)

print(dir(video.link), video.link.streams)
