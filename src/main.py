# LangChain-RAG-Summarizer/src/main.py

"""
main.py
Entry for LangChain RAG Summarizer

Note: Core logic is not currently functional due to drive failure.
Implementation will be restored soon.
"""

from summarizer import generate_summary
from retriever import retrieve_relevant_passage
import json
import os

def run_demo():
    # Load sample data
    data_file = os.path.join(os.path.dirname(__file__), "../data/sample_squad.json")
    with open(data_file, "r") as f:
        dataset = json.load(f)
    question = dataset[0]['question']
    context = retrieve_relevant_passage(question, dataset)
    summary = generate_summary(context)
    print("Question:", question)
    print("Context:", context)
    print("Summary:", summary)

if __name__ == "__main__":
    run_demo()