from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

# Get the video link from user input
lk = input("Video Link: ")

try:
    # Initialize the YouTube object
    link = YouTube(lk)
    
    # Get the video stream with the highest resolution
    video = link.streams.get_highest_resolution()
    
    # Download the video
    video.download()
    print("Download successful!")

except RegexMatchError:
    print("The provided link is not a valid YouTube URL. Please check the format.")

except VideoUnavailable:
    print("The video is unavailable. It may be private or removed.")

except Exception as e:
    # Catch any other exceptions
    print(f"An error occurred: {e}")
