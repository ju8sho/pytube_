
from pytube import YouTube

def yuklaYT(link):
    #
    yt = YouTube(link)

    formats = yt.streams.filter(file_extension='mp4', adaptive=True)
    for index, farmat in enumerate(formats):
        print(f"{index+1}. {farmat}")
    yukla = int(input('Hoxlagan formatni tanlang: '))
    formats[yukla-1].download()
    return 'Video yuklandi'

if __name__ == '__main__':
    link = input('youtube linkni kiriting: ')
    yuklaYT(link)