import math
import os
import re
import sys

from pytube import Playlist, YouTube
from pytube.cli import on_progress


def show_menu():
    print("-------------------- Download Manager---------------------------")
    print("1. Youtube Video Downloader")
    print("2. Youtube Playlist Videos Downloader")


def show_quilites():
    print("1. Low")
    print("2. Medium")
    print("3. High")


def get_mode(modes_list):
    mode = input("> Enter the mode: ")
    if mode not in modes_list:
        print("Invalid mode.")
        get_mode(modes_list)
    return mode


def get_quility():
    options = {
        "1": "low",
        "2": "medium",
        "3": "high",
    }
    quaility = input("> Enter the quaility: ")
    if quaility not in options.keys():
        print("Invalid option.")
        get_mode(options.keys())
    return options.get(quaility)


def dowload_youtube_video(url, quaility="medium"):
    video_url = url
    yt = YouTube(
        video_url,
        on_progress_callback=on_progress,
        on_complete_callback=download_complete,
    )

    print(f"{yt.title} ({yt.length / 60} min)")
    # print("Description: ", yt.description)
    # print("Ratings: ", yt.rating)
    print("Start downloading...")

    # audioStreams = yt.streams.filter(only_audio=True)
    videoStreams = yt.streams.filter(progressive=True).order_by("resolution")

    # subtitles = yt.captions
    # engSubtitle = subtitles.get("en")

    # filedir = os.path.join("/home/ali/Downloads/youtube-downloader/")
    filedir = os.path.join("C:\\Users\\mohamm_ali\\Downloads\\pyScript-downloader\\")

    match quaility.lower().strip():
        case "low":
            videoStreams[0].download(filedir)
        case "medium":
            idx = math.ceil(len(videoStreams) / 2)
            idx = idx - 1
            videoStreams[idx].download(filedir)
        case "high":
            videoStreams[-1].download(filedir)


def download_youtube_playlist(url, quaility="medium"):
    pl = Playlist(url)
    for idx, video in enumerate(pl):
        # print(f"idx={idx}, {type(idx)} ---- video={video}")
        print(f"Downloading video {pl.title} - {idx+1} of {len(pl)}")
        dowload_youtube_video(video, quaility)


def download_complete(*args, **kwargs):
    print("Done.")


if __name__ == "__main__":
    show_menu()
    mode = get_mode(modes_list=["1", "2"])
    url = input("> Enter the URL: ")
    show_quilites()
    match mode:
        case "1":
            dowload_youtube_video(url, quaility=get_quility())
        case "2":
            download_youtube_playlist(url, quaility=get_quility())
