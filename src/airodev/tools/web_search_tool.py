from crewai_tools import BaseTool

class WebSearchTool(BaseTool):
    name = "WebSearchTool"
    description = "Searches the web for similar websites to use as inspiration."

    def _run(self, query: str) -> str:
        # Placeholder: Simulate web search
        return (
            f"Top 3 similar websites found for '{query}':\n"
            "- https://example1.com\n"
            "- https://example2.com\n"
            "- https://example3.com"
        )
