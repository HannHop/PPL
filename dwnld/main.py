import sys
import subprocess
# import yt_dlp
URLS = 'https://www.youtube.com/watch?v=Wq4tyDRhU_4&ab_channel=Editors'
chosen_name_1 = "-o"
chosen_name_2 = "%(title)s.%(ext)s"
chosen_format_1 = "-x"
chosen_format_2 = "--audio-format"
chosen_format_3 = "mp3"
where_1 = "--ffmpeg-location"
where_2 = "./bin/ffmpeg.exe"
subprocess.run(['yt-dlp.exe', chosen_name_1, chosen_name_2, URLS,
                chosen_format_1, chosen_format_2, chosen_format_3, where_1, where_2], check=True)
# subprocess.run([sys.executable, './bin/ffprobe.exe'], check=True)
# subprocess.run([sys.executable, './bin/ffmpeg.exe'], check=True)


ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

#with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#    error_code = ydl.download(URLS)

# print('Some videos failed to download' if error_code
#       else 'All videos successfully downloaded')
