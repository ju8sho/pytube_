from pytube import YouTube

url = 'https://www.youtube.com/shorts/od_PK-S1rYQ'
yt = YouTube(url)

fltr = yt.streams.filter(file_extension='mp4', adaptive=True)

for item, format in enumerate(fltr):
    print(f'{item+1}. {format}')
