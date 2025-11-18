# 🌍 Multilingual Speech Intelligence System

The Multilingual Speech Intelligence System automates multilingual conversation analysis using advanced speech recognition and natural language models. It provides transcription, translation, bilingual summaries, emotion detection, background detection, voice matching, and speaker biographics for languages including Dari, Pashto, Urdu, Arabic, and English.

---

## 🚀 Features
- 🎙️ Multilingual Speech Transcription  
- 🌐 Language Detection  
- 🔁 Translation (multi-target)  
- ✍️ Bilingual Summaries  
- 😊 Emotion Detection  
- 🎧 Background/Noise Detection  
- 🗣️ Voice Matching  
- 👤 Speaker Biographics Inference  

---

## 📁 Project Structure
Multilingual-Speech-Intelligence/
│
├── bilingual_summarizer/
│ ├── init.py
│ ├── summarizer.py
│ ├── translator.py
│ └── utils.py
│
├── models/ # speech & NLP models stored here
│
├── app.py # main execution script
├── main.py # optional pipeline runner
├── requirements.txt
├── README.md
└── LICENSE


## 🛠️ Installation
### 1. Clone the repository

git clone https://github.com/<your-username>/Multilingual-Speech-Intelligence.git
cd Multilingual-Speech-Intelligence

2. Create virtual environment
python -m venv env
source env/bin/activate    # macOS/Linux
env\Scripts\activate       # Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Usage
Transcribe audio
python app.py --audio input.wav

Bilingual summary
python app.py --audio input.wav --summary --src en --tgt ar
