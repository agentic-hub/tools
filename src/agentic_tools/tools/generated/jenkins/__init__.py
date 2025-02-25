# jenkins toolkit
from langchain.tools import BaseTool
from typing import List

def get_jenkins_tools() -> List[BaseTool]:
    """Get all jenkins tools."""
    from . import operations
    return operations.get_tools()

class JenkinsToolkit:
    """Toolkit for interacting with jenkins."""

    def __init__(self):
        """Initialize the jenkins toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all jenkins tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all jenkins tools with default credentials."""
        return get_jenkins_tools()
