import os


class AgenticHubToolkit:
    def __init__(self):
        """Initialize the toolkit with default settings."""
        self.tools = []
        self.api_key = os.getenv("AGENTICHUB_API_KEY")
        if not self.api_key:
            raise ValueError("AGENTICHUB_API_KEY environment variable not set.")

    def add_tool(self, tool):
        """Add a tool to the toolkit."""
        self.tools.append(tool)

    def list_tools(self):
        """List all tools in the toolkit."""
        return self.tools
