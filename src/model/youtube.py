from pytube import YouTube
import os

video_directory = "D:/Studies/Code/Python/DataThrone/youtube_video"

def download(link):
    try:
        youtube_object = YouTube(link)
    except:
        print("Invalid link")
        return False
    
    try:
        if os.path.exists(video_directory):
            os.chdir(video_directory)

            if len(os.listdir(video_directory)) > 0:
                for file in os.listdir(video_directory):
                    os.remove(file)
        else:
            os.mkdir(video_directory)

        if os.getcwd != video_directory:
            os.chdir(video_directory)

        youtube_object = youtube_object.streams.get_highest_resolution()
        youtube_object.download()
    except:
        print("Something went wrong while downloading the youtube video")
        return False

    video_path = os.listdir(video_directory)[0] 
    return True, video_path
    

if __name__  == "__main__":
    link = input("Enter a youtube link: ")
    download(link)