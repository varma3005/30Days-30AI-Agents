# 📰 ➡️ 🎙️ Blog to Podcast Agent

Convert any blog article into a spoken podcast using AI — just paste a URL and get an audio file in seconds.

---

## How It Works

1. You paste a blog URL into the app
2. An AI agent scrapes and reads the article
3. Mistral AI summarizes it into a conversational podcast script
4. gTTS converts the script into spoken audio
5. You listen or download the mp3

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Agno](https://github.com/agno-agi/agno) | Agent framework |
| [Mistral AI](https://mistral.ai/) | LLM for summarization |
| [Newspaper4k](https://github.com/AndyTheFactory/newspaper4k) | Web article scraping |
| [gTTS](https://gtts.readthedocs.io/) | Text to speech |
| [Streamlit](https://streamlit.io/) | Web UI |

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/blog-to-podcast.git
cd blog-to-podcast
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your API key
You only need one API key — **Mistral AI** (free, no credit card required):

1. Go to [console.mistral.ai](https://console.mistral.ai)
2. Sign up and click **API Keys** in the sidebar
3. Click **Create new key** and copy it

### 4. Run the app
```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser (usually `http://localhost:8501`)
2. Paste your **Mistral API key** in the sidebar
3. Enter a blog URL in the input field
4. Click **🎙️ Generate Podcast**
5. Listen in the browser or click **Download Podcast** to save the mp3

---

## Requirements

```
agno
mistralai
streamlit
newspaper4k
lxml_html_clean
certifi
gtts
```

---

## URLs That Work Well

Newspaper4k works best with open, public blogs. Use these types of sites:

✅ Works well:
- `thepythoncode.com`
- `learnpython.com/blog`
- `thenewstack.io`
- `hostinger.com/tutorials`

❌ Avoid (blocks scrapers):
- `medium.com` → 403 error
- `netflixtechblog.com` → SSL issues
- `devops.com` → 403 error

---

## Project Structure

```
blog-to-podcast/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `401 Unauthorized` | Wrong API key | Get a fresh key from console.mistral.ai |
| `403 Forbidden` | Site blocks scrapers | Try a different blog URL |
| `SSL Certificate Error` | Python SSL issue | Already fixed in code via certifi |
| `404 Not Found` | Article deleted/moved | Try a different URL |

---

## Limitations

- gTTS requires an internet connection to generate audio
- Very long articles are trimmed to avoid hitting model limits
- Some websites actively block automated scraping

---

## License

MIT License — free to use and modify.