# 🎵 YouTube Mashup Generator

## 📌 Overview

This project implements a **Mashup Generator** that downloads videos of a specified singer from YouTube, converts them into audio files, trims them to a fixed duration, and merges them into a single output audio file.

The project includes:

- **Program 1 (Required): Command Line Mashup Generator**
- **Program 2 (Required): Web Service with Email Delivery**

---

## 🚀 Program 1 – Command Line Mashup

### ▶️ Usage

python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

### ✅ Example

python 102303280.py "Sharry Maan" 20 20 output.mp3

---

### 📥 Parameters

- **SingerName** – Name of the singer  
- **NumberOfVideos** – Number of videos to download (must be > 10)  
- **AudioDuration** – Duration in seconds to trim (must be > 20)  
- **OutputFileName** – Name of the final merged audio file  

---

### 🔎 Validation Requirements

The program checks for:

- Correct number of arguments  
- Valid numeric inputs  
- NumberOfVideos > 10  
- AudioDuration > 20  
- Proper exception handling  
- Appropriate error messages for invalid inputs  

---

## 🌐 Program 2 – Web Service Mashup

A web-based service that allows users to generate mashups via browser.

### 📝 User Inputs Required

- Singer Name  
- Number of Videos  
- Duration of Each Video  
- Email ID  

### 📤 Output

- The generated mashup file is compressed into ZIP format  
- The ZIP file is sent to the provided email address  

### ✅ Validation

- All fields are mandatory  
- Email ID must be valid  
- Number of videos must be greater than 10  
- Duration must be greater than 20 seconds  
- Proper error handling implemented  

---

## 🛠 Technologies Used

- Python 3.x  
- yt-dlp / pytube (YouTube downloading)  
- moviepy / pydub (Audio processing)  
- Flask (Web service)  
- smtplib (Email sending)  
- zipfile (File compression)  

---

## ⚙️ Installation

Clone the repository:

git clone <https://github.com/Tamannabhardwajj/mashup>  
cd <mashup>

Install dependencies:

pip install -r requirements.txt

---

## ▶️ Running the Command Line Program

python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

---

## ▶️ Running the Web Service

python web_service.py

Open in browser:

http://127.0.0.1:5000/

---

## 📌 Notes

- Ensure stable internet connection while downloading videos.  
- Large number of videos may increase processing time.  
- Email credentials must be configured properly before sending emails.  
- All required dependencies are listed in requirements.txt.  

---

## 👩‍💻 Author

Tamanna Bhardwaj

