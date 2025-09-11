# src/downloader.py

import subprocess
import os
import shlex

def download_media(video_url: str, download_type: str, output_path: str = None) -> None:
    """
    Downloads a video or audio file from a YouTube URL.

    Args:
        video_url: The URL of the YouTube video.
        download_type: The type of download ('audio', 'video', or 'merged').
        output_path: The optional path to save the downloaded file.
    """
    
    # Define a generic download directory
    download_dir = output_path if output_path else "downloads"
    os.makedirs(download_dir, exist_ok=True)
    
    # 🛠 Build the yt-dlp command based on download type
    if download_type == "audio":
        cmd = (
            f'yt-dlp -x --audio-format mp3 '
            f'-o "{download_dir}/%(title)s.%(ext)s" "{video_url}"'
        )
    elif download_type == "video":
        cmd = (
            f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" '
            f'--merge-output-format mp4 '
            f'-o "{download_dir}/%(title)s.%(ext)s" "{video_url}"'
        )
    elif download_type == "merged":
        # This is for merging the video and audio streams
        cmd = (
            f'yt-dlp -f "bestvideo+bestaudio/best" '
            f'--merge-output-format mp4 '
            f'-o "{download_dir}/%(title)s.%(ext)s" "{video_url}"'
        )
    else:
        raise ValueError(f"❌ Invalid download_type: {download_type}. Must be 'audio', 'video', or 'merged'.")
    
    # 🔍 Split the command safely for subprocess
    full_cmd = shlex.split(cmd)

    # 🚀 Execute the command with real-time output
    try:
        print(f"🛠 Running command: {' '.join(full_cmd)}")
        process = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
        
        process.wait()

        if process.returncode == 0:
            print(f"\n✅ Download successful! File saved to {download_dir}")
        else:
            print(f"\n❌ Download failed with return code {process.returncode}.")
            
    except FileNotFoundError as e:
        print(f"❌ Error: The command '{e.filename}' was not found. Please ensure yt-dlp is installed and in your system PATH.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage for testing purposes
    # Note: For the actual project, this should be called from main.py or the jupyter notebook.
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print(f"--- Downloading audio from {test_url} ---")
    download_media(test_url, "audio")
    print(f"\n--- Downloading merged video from {test_url} ---")
    download_media(test_url, "merged")
