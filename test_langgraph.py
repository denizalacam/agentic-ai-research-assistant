from graph.workflow import build_graph


graph = build_graph()

test_questions = [
    "What is 15% of 280?",
    "What do my local documents say about RAG?",
    "What are the latest generative AI applications in healthcare?",
    "Find recent PubMed papers about Alzheimer's disease and transformer models.",
    "Write a literature review on transformer models for Alzheimer's disease diagnosis.",
    "Explain the difference between predictive AI and generative AI.",
]

for question in test_questions:
    print("\n" + "=" * 80)
    print(f"QUESTION: {question}")
    print("=" * 80)

    result = graph.invoke({"question": question})

    print("\nANSWER:\n")
    print(result["final_answer"])