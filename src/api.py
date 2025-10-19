# LangChain-RAG-Summarizer/src/api.py

"""
api.py

Flask API for LangChain-RAG-Summarizer.

Note: Real summarization and retrieval endpoints will be restored soon.
"""

from flask import Flask, request, jsonify
from summarizer import generate_summary
from retriever import retrieve_relevant_passage
import json
import os

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    context = data.get('context', '')
    # TODO: Implement summary logic here when restored
    summary = generate_summary(context)
    return jsonify({"summary": summary})

@app.route('/retrieve_and_summarize', methods=['POST'])
def retrieve_and_summarize():
    data = request.json
    question = data.get('question', '')
    # TODO: Implement retrieval and summary logic when ready
    data_file = os.path.join(os.path.dirname(__file__), "../data/sample_squad.json")
    with open(data_file, "r") as f:
        dataset = json.load(f)
    context = retrieve_relevant_passage(question, dataset)
    summary = generate_summary(context)
    return jsonify({"context": context, "summary": summary})

if __name__ == "__main__":
    app.run(debug=True)