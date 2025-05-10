# 📰 Brochure Generator

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen?logo=streamlit)](https://brochure-generator.streamlit.app/)

Generate a markdown brochure for any company website using Llama3.2 and actual clickable links.  
This project scrapes a company's website, extracts relevant information, and uses a local LLM (Llama3.2 via Ollama) to generate a fun, informative brochure.  
You can use the app via a **Streamlit UI**.

---

![alt text](img/0510.gif)

---

## Try it online

👉 **[Launch the app on Streamlit Cloud](https://brochure-generator.streamlit.app/)**

---

## Features

- Scrape landing and relevant pages from any company website.
- Use Llama3.2 (via Ollama) to generate a markdown brochure.
- All links (social media, partners, etc.) are real and clickable.
- Simple Streamlit web UI.

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) running locally with `llama3.2` model pulled

### Python packages

```
pip install -r requirements.txt
```

Example `requirements.txt`:
```
streamlit
requests
beautifulsoup4
markdown
```

---

## Folder Structure

```
brochure-generator/
│
├─ app.py
├─ requirements.txt
├─ README.md
├─ brochure/
│    ├─ __init__.py
│    ├─ webscrapper.py
│    ├─ llm.py
│    └─ brochure.py
└─ notebooks/
     └─ test.ipynb
```

---

## Usage

### 1. Start Ollama and pull the model

```sh
ollama pull llama3.2
ollama serve
```

### 2. Run the Streamlit app

```sh
streamlit run app.py
```

### 3. Open your browser

Go to [http://localhost:8501](http://localhost:8501) and use the UI to generate brochures.

---

## Customization

- To change the LLM prompt or output style, edit `brochure/brochure.py` and `brochure/llm.py`.
- To add more scraping logic, edit `brochure/webscrapper.py`.

---

## Troubleshooting

- **LLM response parsing error:**  
  The LLM sometimes returns non-JSON output. The code tries to extract JSON, but you may need to adjust prompts or parsing logic.

---

## Credits

- [Ollama](https://ollama.com/)
- [Llama3.2](https://ollama.com/library/llama3)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---

Happy brochure generating!
