# metabase toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_metabase_tools() -> List[BaseTool]:
    """Get all metabase tools."""
    from . import operations
    return operations.get_tools()

class MetabaseCredentials(BaseModel):
    """Credentials for metabase authentication."""
    metabase_api: Optional[Dict[str, Any]] = Field(None, description="metabaseApi")

class MetabaseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with metabase."""

    def __init__(self, credentials: Optional[MetabaseCredentials] = None):
        """Initialize the metabase toolkit with optional credentials.

        Args:
            credentials: MetabaseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all metabase tools with the configured credentials."""
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
        """Get all metabase tools with default credentials."""
        return get_metabase_tools()
