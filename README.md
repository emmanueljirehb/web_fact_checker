# 🔎 Web Fact Checker using Crew AI



<img width="2048" height="2048" alt="Gemini_Generated_Image_g06iqg06iqg06iqg" src="https://github.com/user-attachments/assets/3f0457ef-a728-4676-a875-b5e8858b948f" />




This project is an **autonomous fact-checking application** that uses [CrewAI](https://github.com/joaomdmoura/crewai) agents to:
- 🔍 Extract factual claims from a website
- 🧠 Verify those claims using real-time web search (via Serper)
- 📝 Summarize the findings with verdicts

Built with **Python, Streamlit, and CrewAI**, it provides a simple UI where users can paste a website URL and get a fact-checking report in seconds.

---

## 🚀 Features

- ✅ URL-based claim extraction and verification
- 🤖 Three autonomous agents:
  - `Claim Extractor`
  - `Fact Verifier`
  - `Summary Reporter`
- 🔍 Real-time web search using Serper
- 🧾 Markdown-formatted output with verdicts
- 📥 Downloadable summary report

---

## 🧠 Agents Overview

| Agent Name       | Role                  | Description                                      |
|------------------|-----------------------|--------------------------------------------------|
| Claim Extractor  | Extracts claims       | Parses webpage to identify factual claims        |
| Fact Verifier    | Verifies each claim   | Uses Serper search to check accuracy             |
| Summary Reporter | Summarizes findings   | Writes clear verdict and final report            |

---

## 🧩 Tech Stack

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Streamlit](https://streamlit.io/)
- [Serper API](https://serper.dev) for web search
- OpenAI GPT-4 (or GPT-3.5)

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/web_fact_checker.git
cd web_fact_checker
```

## 🔧 Setup Instructions

### 2. Create and Activate a Virtual Environment

```
python -m venv .venv
```
### For Windows
.venv\Scripts\activate

### For macOS/Linux
source .venv/bin/activate


### 📄 `README.md`


# 🔎 Web Fact Checker using CrewAI

This project is an **autonomous fact-checking application** that uses [CrewAI](https://github.com/joaomdmoura/crewai) agents to:
- 🔍 Extract factual claims from a website
- 🧠 Verify those claims using real-time web search (via Serper)
- 📝 Summarize the findings with verdicts

Built with **Python, Streamlit, and CrewAI**, it provides a simple UI where users can paste a website URL and get a fact-checking report in seconds.

---

## 🚀 Features

- ✅ URL-based claim extraction and verification
- 🤖 Three autonomous agents:
  - `Claim Extractor`
  - `Fact Verifier`
  - `Summary Reporter`
- 🔍 Real-time web search using Serper
- 🧾 Markdown-formatted output with verdicts
- 📥 Downloadable summary report

---

## 🧠 Agents Overview

| Agent Name       | Role                  | Description                                      |
|------------------|-----------------------|--------------------------------------------------|
| Claim Extractor  | Extracts claims       | Parses webpage to identify factual claims        |
| Fact Verifier    | Verifies each claim   | Uses Serper search to check accuracy             |
| Summary Reporter | Summarizes findings   | Writes clear verdict and final report            |

---

## 🧩 Tech Stack

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Streamlit](https://streamlit.io/)
- [Serper API](https://serper.dev) for web search
- OpenAI GPT-4 (or GPT-3.5)

---

## 🛠️ Installation

### 1. Clone the repo


git clone https://github.com/your-username/web_fact_checker.git
cd web_fact_checker


### 2. Create and activate a virtual environment


python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Add your API keys

Create a `.env` file in the project root:


OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key


> ⚠️ **Important**: The `.env` file is excluded via `.gitignore` and should never be pushed to GitHub.

---

## ▶️ Run the App


streamlit run streamlit_app.py


Then open: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
web_fact_checker/
├── streamlit_app.py           # Main Streamlit frontend
├── crew.py                    # Agent/task setup using CrewAI
├── requirements.txt           # Dependencies
├── .gitignore                 # Ignores secrets and cache
├── .env                       # API keys (not committed)
│
├── config/
│   ├── agents.yaml            # Agent configurations
│   └── tasks.yaml             # Task descriptions/prompts
│
└── tools/
    └── custom_tool.py         # Serper search tool
```

---

## 📌 Example Output


✅ Verified:
- "OpenAI released ChatGPT in November 2022"

❌ False:
- "AI can think exactly like humans"

📌 Verdict: The article is generally accurate, but contains some misleading phrasing.



## 💡 Future Ideas

* 🧠 RAG-based document fact-checking
* 🗃️ Save reports to PDF
* 🌐 Deploy on Streamlit Cloud or Hugging Face Spaces

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🤝 Acknowledgments

* [CrewAI](https://github.com/joaomdmoura/crewai)
* [Serper.dev](https://serper.dev)
* [OpenAI](https://openai.com)


---
## 📬 Connect With Me

Like the project? Let’s connect\!

  * 🔗 [GitHub](https://github.com/emmanueljirehb) 
  * 📊 [Kaggle](https://www.kaggle.com/emmanueljireh)
  * 📝 [Medium](https://medium.com/@emmanueljirehb)
  * 💼 [LinkedIn](https://www.linkedin.com/in/emmanueljirehb)

# OUTPUTS



## This is final output of the project in a Webpage


### Project execution Video is posted in linkedin kindly visit this link 


(https://www.linkedin.com/posts/emmanueljirehb_ai-crewai-openai-activity-7358392795260252160-_rGY?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEbghGABnNb43icafqxzvdGO2hRcs8oGW8U)




<img width="1920" height="1080" alt="e5" src="https://github.com/user-attachments/assets/9447e8e6-95fa-4db8-b7f3-1392e1a9d004" />



---



## ' Agent 1 ' in this image  , Extracts the claims given by user and search the internet with the help of " SERPER " tool



<img width="1920" height="1080" alt="e1" src="https://github.com/user-attachments/assets/a4cddee3-f740-4d60-b055-fe1e8ceb154c" />



---



## ' Agent 1 ' in this image  , is searching the website link which is given by user



<img width="1920" height="1080" alt="e2" src="https://github.com/user-attachments/assets/dfc95185-a62d-457b-8a33-69cc25af489f" />



---



## ' Agent 2 ' in this image  , checks the entire website for facts and finally hands it over to Agent 3 



<img width="1920" height="1080" alt="e3" src="https://github.com/user-attachments/assets/7a6bf22a-9d0f-45e8-8de0-0cf0117de903" />



---



## ' Agent 3 ' in this image  , presents the final output i.e the number of facts extracted from a website URL and gives the final outcome in a markdown file in a webpage



<img width="1920" height="1080" alt="e4" src="https://github.com/user-attachments/assets/6c29bd49-7c0b-41d4-a8ad-bdc10fa685b7" />





