# segment toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_segment_tools() -> List[BaseTool]:
    """Get all segment tools."""
    from . import operations
    return operations.get_tools()

class SegmentCredentials(BaseModel):
    """Credentials for segment authentication."""
    segment_api: Optional[Dict[str, Any]] = Field(None, description="segmentApi")

class SegmentToolkit(AgenticHubToolkit):
    """Toolkit for interacting with segment."""

    def __init__(self, credentials: Optional[SegmentCredentials] = None):
        """Initialize the segment toolkit with optional credentials.

        Args:
            credentials: SegmentCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all segment tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        # Apply credentials to each tool if provided
        if self.credentials:
            for tool in tools:
                # Set credentials on each tool instance
                tool.credentials = self.credentials
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all segment tools with default credentials."""
        return get_segment_tools()
