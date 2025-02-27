# facebookgraphapi toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_facebookgraphapi_tools() -> List[BaseTool]:
    """Get all facebookgraphapi tools."""
    from . import operations
    return operations.get_tools()

class FacebookgraphapiCredentials(BaseModel):
    """Credentials for facebookgraphapi authentication."""
    facebook_graph_api: Optional[Dict[str, Any]] = Field(None, description="facebookGraphApi")

class FacebookgraphapiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with facebookgraphapi."""

    def __init__(self, credentials: Optional[FacebookgraphapiCredentials] = None):
        """Initialize the facebookgraphapi toolkit with optional credentials.

        Args:
            credentials: FacebookgraphapiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all facebookgraphapi tools with the configured credentials."""
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
        """Get all facebookgraphapi tools with default credentials."""
        return get_facebookgraphapi_tools()
