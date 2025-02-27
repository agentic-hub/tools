# aggregate toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_aggregate_tools() -> List[BaseTool]:
    """Get all aggregate tools."""
    from . import operations
    return operations.get_tools()

class AggregateToolkit(AgenticHubToolkit):
    """Toolkit for interacting with aggregate."""

    def __init__(self):
        """Initialize the aggregate toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all aggregate tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all aggregate tools with default credentials."""
        return get_aggregate_tools()
