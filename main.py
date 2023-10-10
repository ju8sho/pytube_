from pytube import YouTube

def download_Yt_video(link):

    yt = YouTube(link)
    # info = yt.streams.filter(file_extension=True, adaptive=True)
    # infor = {}
    # for item in info:
    #


    try:
        res = yt.streams.get_by_itag(int(input(">>")))
        res.download()
    except:
        return ('Xatolik yuz berdi!')
    return ('Video yuklandi')

# link = input('URL: ')
# download_Yt_video(link)



if __name__ == '__main__':
    link = input('URL: ')
    download_Yt_video(link)
