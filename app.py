from pytube import YouTube
from moviepy.editor import *
import os
import random
import shutil
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


def download_mp3(link, file_path):

    workdir = str(random.random())
    os.mkdir(workdir)
    save_file_loc = file_path + '/' + workdir
    youtube_obj = YouTube(link)
    resolution = youtube_obj.streams.get_highest_resolution()
    resolution.download(save_file_loc)
    name = os.listdir(save_file_loc)
    video_name = name[0]
    video = VideoFileClip(f"{save_file_loc}/{video_name}")
    video.audio.write_audiofile(f'{video_name}.mp3')
    shutil.rmtree(save_file_loc)
    os.rmdir(workdir)


def download_mp4(link, file_path):

    save_file_loc = file_path
    youtube_obj = YouTube(link)
    resolution = youtube_obj.streams.get_highest_resolution()
    resolution.download(save_file_loc)


print("Choose the preferred format type to download your video.")
file_format = input("Type 'MP3' or 'MP4': ")
format_format = file_format.upper()
if format_format == "MP3":
    download_mp3(link=input("Video link: "), file_path=input("download_location: "))
elif format_format == "MP4":
    download_mp4(link=input("Video Link(MP4): "), file_path=input("download_location: "))
else:
    print("Error occurred!")
    exit()
