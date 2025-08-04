import streamlit as st
from crew import get_url_crew
import os

from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

st.set_page_config(page_title="Web Fact Checker", page_icon="🔎")

st.title("🔎 Web Fact Checker using CrewAI")
st.markdown("Paste a URL below. We'll extract and verify factual claims.")

url = st.text_input("Enter a website URL:", placeholder="https://...")

if st.button("✅ Run Fact Check", use_container_width=True):
    if not url:
        st.warning("Please enter a URL.")
        st.stop()

    with st.spinner("Running agents..."):
        try:
            crew = get_url_crew(url)
            result = crew.kickoff(inputs={"url": url})
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    st.success("✅ Fact-check complete!")
    st.markdown("### 🧾 Result")
    st.code(str(result), language="markdown")
