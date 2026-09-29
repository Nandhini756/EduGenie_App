# EduGenie – AI-Powered Learning Assistant

## 📌 Project Overview

EduGenie is an AI-powered learning assistant designed to help students with their learning and study activities.

The project uses Generative AI to provide multiple learning-support features through a single application. It is designed to make learning easier, more interactive, and more convenient for students.

---

## 🎯 Purpose of the Project

The main purpose of EduGenie is to support students in their learning process using Generative AI.

Students can use EduGenie when they have questions, need explanations, want to summarize study material, practise through quizzes, or need learning recommendations.

The project aims to provide different learning-support features in one application instead of requiring students to use separate tools for different learning activities.

---

## ✨ Features

EduGenie provides five main learning features:

### 1. Question & Answer

Students can enter a question and receive an AI-generated answer related to their query.

### 2. Explanation

Students can enter a topic or concept they find difficult, and EduGenie provides an explanation to help them understand it more easily.

### 3. Summarization

Students can provide longer study material and receive a shorter summary that can be useful for quick revision.

### 4. Quiz Generation

EduGenie can generate quiz questions based on a selected topic, helping students practise and check their understanding.

### 5. Learning Path / Recommendations

EduGenie can provide learning guidance and recommendations based on the topic selected by the student.

---

## 💡 Uses and Benefits

EduGenie can be useful for students in several ways:

- Helps students understand difficult concepts.
- Provides AI-based answers to questions.
- Supports quick revision through summarization.
- Provides quiz-based practice.
- Helps students continue learning through recommendations.
- Saves time by providing multiple learning features in one application.
- Makes learning more interactive.
- Supports self-learning and independent study.
- Provides convenient AI-based learning assistance.

---

## 🛠️ Technologies Used

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Google Gemini API
- Generative AI / Large Language Model (LLM)

---

## 📂 Project Structure

```text
edugenie/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── gemini_client.py
│   │
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── qna.py
│   │   ├── explanation.py
│   │   ├── summary.py
│   │   ├── quiz.py
│   │   └── learning_path.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── app.js
│
├── tests/
│   └── test_api.py
│
├── .env.example
├── .gitignore
├── pyproject.toml
└── requirements.txt
