import streamlit
import json


with open("quiz.json", 'r') as file:
    data = json.load(file)
    file.close()

streamlit.title("Welcome! Do YOU know Roxana? Find out.")

for row in data:
    streamlit.subheader(row["question"])

    for quiz_option in row["answers"]:
        streamlit.checkbox(quiz_option)

