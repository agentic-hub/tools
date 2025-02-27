# airtable toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_airtable_tools() -> List[BaseTool]:
    """Get all airtable tools."""
    from . import operations
    return operations.get_tools()

class AirtableCredentials(BaseModel):
    """Credentials for airtable authentication."""
    airtable_token_api: Optional[Dict[str, Any]] = Field(None, description="airtableTokenApi")
    airtable_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="airtableOAuth2Api")

class AirtableToolkit(AgenticHubToolkit):
    """Toolkit for interacting with airtable."""

    def __init__(self, credentials: Optional[AirtableCredentials] = None):
        """Initialize the airtable toolkit with optional credentials.

        Args:
            credentials: AirtableCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all airtable tools with the configured credentials."""
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
        """Get all airtable tools with default credentials."""
        return get_airtable_tools()
