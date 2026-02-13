import sys
import os
import subprocess
from pydub import AudioSegment


def show_usage():
    print("Usage:")
    print("python <program.py> <Sharry Maan> <NumberOfVideos> <AudioDuration> <OutputFileName>")
    print("Example:")
    print('python 101556.py "Sharry Maan" 20 20 output.mp3')


def download_videos(query, count):

    folder = "videos"
    os.makedirs(folder, exist_ok=True)

    search = f"ytsearch{count}:{query}"

    command = [
        "yt-dlp",
        "-f", "mp4",
        "-o", f"{folder}/%(title)s.%(ext)s",
        search
    ]

    subprocess.run(command)


def convert_to_audio():

    video_folder = "videos"
    audio_folder = "audios"

    os.makedirs(audio_folder, exist_ok=True)

    for file in os.listdir(video_folder):

        if file.endswith(".mp4"):

            video_path = os.path.join(video_folder, file)

            audio_name = file.replace(".mp4", ".mp3")
            audio_path = os.path.join(audio_folder, audio_name)

            sound = AudioSegment.from_file(video_path)
            sound.export(audio_path, format="mp3")


def trim_audio(seconds):

    audio_folder = "audios"
    trimmed_folder = "trimmed"

    os.makedirs(trimmed_folder, exist_ok=True)

    for file in os.listdir(audio_folder):

        if file.endswith(".mp3"):

            path = os.path.join(audio_folder, file)

            audio = AudioSegment.from_mp3(path)

            trimmed = audio[:seconds * 1000]

            new_path = os.path.join(trimmed_folder, file)

            trimmed.export(new_path, format="mp3")


def merge_audio(output):

    folder = "trimmed"

    final = AudioSegment.empty()

    for file in os.listdir(folder):

        if file.endswith(".mp3"):

            path = os.path.join(folder, file)

            audio = AudioSegment.from_mp3(path)

            final += audio

    final.export(output, format="mp3")


def main():

    if len(sys.argv) != 5:
        print("❌ Wrong number of arguments")
        show_usage()
        return

    singer = sys.argv[1]

    try:
        n = int(sys.argv[2])
        y = int(sys.argv[3])
    except:
        print("❌ Number of videos and duration must be numbers")
        return

    output = sys.argv[4]

    if n <= 10:
        print("❌ Number of videos must be > 10")
        return

    if y <= 20:
        print("❌ Duration must be > 20 seconds")
        return

    try:

        print("📥 Downloading videos...")
        download_videos(singer, n)

        print("🎵 Converting to audio...")
        convert_to_audio()

        print("✂ Trimming audio...")
        trim_audio(y)

        print("🔗 Merging audio...")
        merge_audio(output)

        print("✅ Done! Output file:", output)

    except Exception as e:

        print("❌ Error occurred:", e)


if __name__ == "__main__":
    main()