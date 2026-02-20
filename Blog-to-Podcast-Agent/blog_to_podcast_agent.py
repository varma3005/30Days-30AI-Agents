import os
import ssl
import io
import certifi
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.mistral import MistralChat
from agno.tools.newspaper4k import Newspaper4kTools
from gtts import gTTS
import streamlit as st

# Fix SSL error
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

st.set_page_config(page_title="📰 ➡️ 🎙️ Blog to Podcast", page_icon="🎙️")
st.title("📰 ➡️ 🎙️ Blog to Podcast Agent")

st.sidebar.header("🔑 API Keys")
mistral_key = st.sidebar.text_input("Mistral API Key", type="password")
# ✅ No ElevenLabs key needed anymore

url = st.text_input("Enter Blog URL:", "")

if st.button("🎙️ Generate Podcast", disabled=not mistral_key):
    if not url.strip():
        st.warning("Please enter a blog URL")
    else:
        with st.spinner("Scraping blog and generating podcast..."):
            try:
                os.environ["MISTRAL_API_KEY"] = mistral_key

                agent = Agent(
                    name="Blog Summarizer",
                    model=MistralChat(id="mistral-small-latest"),
                    tools=[Newspaper4kTools()],
                    instructions=[
                        "Scrape the blog URL and create a concise, engaging summary (max 2000 characters) suitable for a podcast.",
                        "The summary should be conversational and capture the main points."
                    ],
                )

                response: RunOutput = agent.run(f"Scrape and summarize this blog for a podcast: {url}")
                summary = response.content if hasattr(response, 'content') else str(response)

                if summary:
                   
                    tts = gTTS(text=summary, lang='en', slow=False)
                    audio_buffer = io.BytesIO()
                    tts.write_to_fp(audio_buffer)
                    audio_bytes = audio_buffer.getvalue()

                    st.success("Podcast generated! 🎧")
                    st.audio(audio_bytes, format="audio/mp3")

                    st.download_button(
                        "Download Podcast",
                        audio_bytes,
                        "podcast.mp3",
                        "audio/mp3"
                    )

                    with st.expander("📄 Podcast Summary"):
                        st.write(summary)
                else:
                    st.error("Failed to generate summary")

            except Exception as e:
                st.error(f"Error: {e}")

