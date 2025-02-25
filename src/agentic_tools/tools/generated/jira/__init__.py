# jira toolkit
from langchain.tools import BaseTool
from typing import List

def get_jira_tools() -> List[BaseTool]:
    """Get all jira tools."""
    from . import operations
    return operations.get_tools()

class JiraToolkit:
    """Toolkit for interacting with jira."""

    def __init__(self):
        """Initialize the jira toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all jira tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all jira tools with default credentials."""
        return get_jira_tools()
