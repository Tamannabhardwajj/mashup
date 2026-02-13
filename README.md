🎵 YouTube Mashup Generator

This project implements a Mashup Generator that downloads videos of a specified singer from YouTube, converts them into audio files, trims them to a fixed duration, and merges them into a single output audio file. The project includes both a command-line based solution and a web-based service for automated mashup generation and email delivery.

The system performs the following operations: downloads N videos of a given singer from YouTube, converts each video into audio format, trims the first Y seconds from each audio file, and merges all trimmed audio clips into a single output file. Proper validation and exception handling are implemented to ensure robustness.

Program 1 – Command Line Mashup (Required)

The program must be named in the format <RollNumber>.py.
Example: 101556.py

Usage:

python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Example:

python 101556.py "Sharry Maan" 20 20 output.mp3

Parameters:

SingerName: Name of the singer

NumberOfVideos: Number of videos to download (must be greater than 10)

AudioDuration: Duration in seconds to trim from each audio file (must be greater than 20)

OutputFileName: Name of the final merged output file

The program validates:

Correct number of arguments

Valid numeric inputs

NumberOfVideos > 10

AudioDuration > 20

Proper exception handling with meaningful error messages

Program 2 – Web Service Mashup (Required)

A web-based mashup generator where the user provides:

Singer Name

Number of Videos

Duration of Each Video

Email ID

The system generates the mashup, compresses it into a ZIP file, and sends it to the provided email address. Email format validation and proper error handling are implemented.

Technologies Used

Python 3.x

yt-dlp / pytube for YouTube video downloading

moviepy / pydub for audio processing

Flask for web service

smtplib for email sending

zipfile for file compression

Installation

Clone the repository and install dependencies:

pip install -r requirements.txt

Running Command Line Program

python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

Running Web Service

python web_service.py

Then open: http://127.0.0.1:5000/

Notes

Ensure stable internet connection while downloading videos.

Large number of videos may increase processing time.

Email credentials must be configured properly before sending mails.

All dependencies are listed in requirements.txt.

Author: Tamanna Bhardwaj
