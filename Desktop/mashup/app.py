import os
import yt_dlp
import zipfile
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
from pydub import AudioSegment

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
OUTPUT_FOLDER = "output"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ---------------- DOWNLOAD FROM YOUTUBE ----------------
def download_songs(singer, num_videos):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True
    }

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


# ---------------- CREATE MASHUP ----------------
def create_mashup(duration):
    mashup = AudioSegment.empty()

    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.endswith((".webm", ".m4a", ".mp3")):
            audio = AudioSegment.from_file(os.path.join(DOWNLOAD_FOLDER, file))
            trimmed = audio[:duration * 1000]
            mashup += trimmed

    output_path = os.path.join(OUTPUT_FOLDER, "mashup.mp3")
    mashup.export(output_path, format="mp3")

    return output_path


# ---------------- CREATE ZIP ----------------
def create_zip(file_path):
    zip_path = os.path.join(OUTPUT_FOLDER, "mashup.zip")

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))

    return zip_path


# ---------------- SEND EMAIL ----------------
def send_email(receiver_email, zip_path):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Your mashup file is attached.")

    with open(zip_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
                           subtype="zip", filename="mashup.zip")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


# ---------------- ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        num_videos = int(request.form["num_videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        # Clear old files
        for f in os.listdir(DOWNLOAD_FOLDER):
            os.remove(os.path.join(DOWNLOAD_FOLDER, f))

        # Steps
        download_songs(singer, num_videos)
        mashup_path = create_mashup(duration)
        zip_path = create_zip(mashup_path)
        send_email(email, zip_path)

        return "<h2>Mashup created and sent to your email!</h2>"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
