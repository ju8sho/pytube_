from pytube import YouTube

video_url = 'https://www.youtube.com/shorts/od_PK-S1rYQ'
youtube = YouTube(video_url)

formats = youtube.streams.all()

for index, format in enumerate(formats):
    print(f"{index+1}. {format}")

# select_format = int(input('Format raqamini kiriting: '))
# formats[select_format-1].download()

