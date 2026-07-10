from rich.console import Console
from agents.research_agent import ResearchAgent

# Create a colorful console
console = Console()
agent = ResearchAgent()

console.print("[bold green]🚀 Agentic AI Research Assistant[/bold green]\n")

question = input("Ask a research question: ")

answer = agent.answer(question)

console.print("\n[bold blue]Answer:[/bold blue]\n")
console.print(answer)