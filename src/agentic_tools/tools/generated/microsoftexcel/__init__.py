# microsoftexcel toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsoftexcel_tools() -> List[BaseTool]:
    """Get all microsoftexcel tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftexcelCredentials(BaseModel):
    """Credentials for microsoftexcel authentication."""
    microsoft_excel_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftExcelOAuth2Api")

class MicrosoftexcelToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsoftexcel."""

    def __init__(self, credentials: Optional[MicrosoftexcelCredentials] = None):
        """Initialize the microsoftexcel toolkit with optional credentials.

        Args:
            credentials: MicrosoftexcelCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftexcel tools with the configured credentials."""
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
        """Get all microsoftexcel tools with default credentials."""
        return get_microsoftexcel_tools()
