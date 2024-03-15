from pytube import YouTube
import os

video_directory = "D:/Studies/Code/Python/DataThrone/public/"

def download(link):
    try:
        youtube_object = YouTube(link)
    except:
        print("Invalid link")
        return False
    
    try:
        if os.getcwd != video_directory:
            os.chdir(video_directory)

        youtube_object = youtube_object.streams.get_highest_resolution()
        youtube_object.download()
    except:
        print("Something went wrong while downloading the youtube video")
        return False

    print("Video downloaded successfuly")
    return True
    

if __name__  == "__main__":
    link = input("Enter a youtube link: ")
    download(link)