from graph.workflow import build_graph


graph = build_graph()

result = graph.invoke(
    {
        "question": "Find recent PubMed papers about Alzheimer's disease."
    }
)

print(result)