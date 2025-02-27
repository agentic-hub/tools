# code toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_code_tools() -> List[BaseTool]:
    """Get all code tools."""
    from . import operations
    return operations.get_tools()

class CodeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with code."""

    def __init__(self):
        """Initialize the code toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all code tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all code tools with default credentials."""
        return get_code_tools()
