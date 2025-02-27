# splitinbatches toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_splitinbatches_tools() -> List[BaseTool]:
    """Get all splitinbatches tools."""
    from . import operations
    return operations.get_tools()

class SplitinbatchesToolkit(AgenticHubToolkit):
    """Toolkit for interacting with splitinbatches."""

    def __init__(self):
        """Initialize the splitinbatches toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all splitinbatches tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all splitinbatches tools with default credentials."""
        return get_splitinbatches_tools()
