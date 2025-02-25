# grafana toolkit
from langchain.tools import BaseTool
from typing import List

def get_grafana_tools() -> List[BaseTool]:
    """Get all grafana tools."""
    from . import operations
    return operations.get_tools()

class GrafanaToolkit:
    """Toolkit for interacting with grafana."""

    def __init__(self):
        """Initialize the grafana toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all grafana tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all grafana tools with default credentials."""
        return get_grafana_tools()
