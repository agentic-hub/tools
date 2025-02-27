# getresponse toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_getresponse_tools() -> List[BaseTool]:
    """Get all getresponse tools."""
    from . import operations
    return operations.get_tools()

class GetresponseCredentials(BaseModel):
    """Credentials for getresponse authentication."""
    get_response_api: Optional[Dict[str, Any]] = Field(None, description="getResponseApi")
    get_response_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="getResponseOAuth2Api")

class GetresponseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with getresponse."""

    def __init__(self, credentials: Optional[GetresponseCredentials] = None):
        """Initialize the getresponse toolkit with optional credentials.

        Args:
            credentials: GetresponseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all getresponse tools with the configured credentials."""
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
        """Get all getresponse tools with default credentials."""
        return get_getresponse_tools()
