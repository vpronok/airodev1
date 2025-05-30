from crewai_tools import BaseTool

class RecallTool(BaseTool):
    name = "RecallTool"
    description = "Learns from past project inputs and outputs to improve future results."

    memory = []

    def _run(self, data: dict) -> str:
        self.memory.append(data)
        return f"Stored project data for learning: {data.get('project_name', 'unnamed')}"

    def recall(self, keyword: str) -> list:
        return [entry for entry in self.memory if keyword in str(entry)]
