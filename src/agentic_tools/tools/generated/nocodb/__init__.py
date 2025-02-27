# nocodb toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_nocodb_tools() -> List[BaseTool]:
    """Get all nocodb tools."""
    from . import operations
    return operations.get_tools()

class NocodbCredentials(BaseModel):
    """Credentials for nocodb authentication."""
    noco_db: Optional[Dict[str, Any]] = Field(None, description="nocoDb")
    noco_db_api_token: Optional[Dict[str, Any]] = Field(None, description="nocoDbApiToken")

class NocodbToolkit(AgenticHubToolkit):
    """Toolkit for interacting with nocodb."""

    def __init__(self, credentials: Optional[NocodbCredentials] = None):
        """Initialize the nocodb toolkit with optional credentials.

        Args:
            credentials: NocodbCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all nocodb tools with the configured credentials."""
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
        """Get all nocodb tools with default credentials."""
        return get_nocodb_tools()
