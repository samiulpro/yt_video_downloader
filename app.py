from pytube import YouTube

def download_mp3(link, file_path):

    save_file_loc = file_path
    youtube_obj = YouTube(link)
    resolution = youtube_obj.streams.filter(only_audio=True).first()
    resolution.download(save_file_loc)


def download_mp4(link, file_path):

    save_file_loc = file_path
    youtube_obj = YouTube(link)
    resolution = youtube_obj.streams.get_highest_resolution()
    resolution.download(save_file_loc)


print("Choose the prefered format type to download your video.")
format = input("Type 'MP3' or 'MP4': ")
format_format = format.upper()
if format_format == "MP3":
    download_mp3(link=input("Video link: "), file_path=input("download_location: "))
elif format_format == "MP4":
    download_mp4(link=input("Video Link(MP4): "), file_path=input("download_location: "))
else:
    print("Error occured!")
    exit()