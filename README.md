# 🧠 Offline NLP Chatbot (Python)

A lightweight NLP-based chatbot that runs entirely offline using text preprocessing and fuzzy intent matching. The project demonstrates how conversational systems can be built without cloud APIs, external AI services, or internet connectivity.

---

## 🚀 Overview

This project implements a rule-based conversational assistant that identifies user intent through fuzzy string matching and returns predefined responses from a structured JSON knowledge base.

The chatbot processes user input locally, making it suitable for learning NLP fundamentals and building low-resource conversational systems.

---

## ✨ Features

* Offline operation with no external API dependency
* Text preprocessing and normalization
* Intent recognition using fuzzy string matching
* JSON-based response management
* Fallback handling for unknown queries
* Lightweight and low-latency execution
* Command-line chat interface

---

## ⚙️ How It Works

### Processing Pipeline

```text
User Input
    ↓
Text Preprocessing
    ↓
Intent Matching (Fuzzy Similarity)
    ↓
Best Intent Selection
    ↓
Response Retrieval from JSON
    ↓
Bot Response
```

### Core Components

#### Text Preprocessing

The chatbot normalizes user input by:

* Converting text to lowercase
* Removing punctuation and special characters

This helps improve matching consistency.

#### Intent Recognition

Instead of exact keyword matching, the chatbot uses fuzzy string similarity to compare user input against predefined intents.

Example:

```text
User Input: "helo"
Known Intent: "hello"

Similarity Score: High
Response: "Hello! How can I help you?"
```

This allows the chatbot to handle minor spelling variations and input inconsistencies.

#### Response Routing

Responses are stored in a JSON file, making it easy to add or modify intents without changing the chatbot logic.

---

## 🛠 Tech Stack

* Python
* FuzzyWuzzy
* JSON
* Regular Expressions (re)
* PyPDF (currently included for future document-processing extensions)

---

## 📂 Project Structure

```text
chatbot_project/
├── chatbot.py
├── responses.json
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python chatbot.py
```

---

## 💬 Example Conversation

```text
You: hello
Bot: Hello! How can I help you?

You: how are you
Bot: I am functioning properly.

You: who created you
Bot: I was created by Vivek.

You: random question
Bot: Sorry, I don't understand.
```

---

## 📚 Learning Outcomes

This project demonstrates:

* Basic Natural Language Processing (NLP)
* Text normalization techniques
* Intent-based chatbot architecture
* Approximate string matching
* Structured response management
* Local-first software design

---

## 🔮 Future Improvements

Possible enhancements include:

* PDF document querying
* Resume or document parsing
* TF-IDF based matching
* Semantic similarity search
* Machine learning based intent classification
* Retrieval-Augmented Generation (RAG)
* Web interface using Flask

---

## 🎯 Use Cases

* NLP learning projects
* Educational demonstrations
* Offline conversational systems
* Low-resource environments
* Prototype virtual assistants

---

## 👨‍💻 Author

**Vivek Devda**
B.Tech Artificial Intelligence & Machine Learning

---

## License

This project is intended for educational and learning purposes.
