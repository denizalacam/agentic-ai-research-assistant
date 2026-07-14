from graph.workflow import build_graph


def main():
    print("🚀 Agentic AI Research Assistant\n")

    question = input("Ask a research question: ")

    graph = build_graph()
    result = graph.invoke(
        {
            "question": question,
        }
    )

    print("\nAnswer:\n")
    print(result["final_answer"])


if __name__ == "__main__":
    main()