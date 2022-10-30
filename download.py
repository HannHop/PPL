import subprocess

chosen_name_1 = "-o"
chosen_name_2 = "%(title)s.%(ext)s"
chosen_format_1 = "-x"
chosen_format_2 = "--audio-format"
chosen_format_3 = "mp3"
where_1 = "--ffmpeg-location"
where_2 = "./bin/ffmpeg.exe"
output_path_flag = "--paths"

abort = False


def abort_downloads():
    global abort
    abort = True


def download_urls(urls, output_path, on_event):
    global abort
    abort = False

    for i in range(len(urls)):
        cmd = ' '.join([
            'yt-dlp.exe',
            chosen_name_1, chosen_name_2,
            urls[i],
            chosen_format_1, chosen_format_2, chosen_format_3,
            where_1, where_2,
        ])

        if output_path != '':
            cmd += ' '
            cmd += output_path_flag
            cmd += ' '
            cmd += output_path

        process = subprocess.Popen(
            cmd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        while True:
            line = process.stdout.readline()
            print(line)
            on_event(line)

            if abort:
                process.terminate()
                on_event("Process killed")

            if process.poll() is not None:
                break

    on_event("Downloaded")

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}
