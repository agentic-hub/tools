# noop toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_noop_tools() -> List[BaseTool]:
    """Get all noop tools."""
    from . import operations
    return operations.get_tools()

class NoopToolkit(AgenticHubToolkit):
    """Toolkit for interacting with noop."""

    def __init__(self):
        """Initialize the noop toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all noop tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all noop tools with default credentials."""
        return get_noop_tools()
