import os
import importlib.util
import subprocess

# Check if pytube is installed, if not, install it
def check_installation(package):
    spec = importlib.util.find_spec(package)
    if spec is None:
        print(f"{package} is not installed. Installing now...")
        subprocess.check_call(['pip', 'install', package])

# Check and install pytube
check_installation("pytube")

from pytube import YouTube

def download_video(url, output_dir):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_path = os.path.join(output_dir, "video.mp4")
        stream.download(output_dir)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_dir = "videos"
    
    # Create the 'videos' directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    download_video(video_url, output_dir)
