# agilecrm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_agilecrm_tools() -> List[BaseTool]:
    """Get all agilecrm tools."""
    from . import operations
    return operations.get_tools()

class AgilecrmCredentials(BaseModel):
    """Credentials for agilecrm authentication."""
    agile_crm_api: Optional[Dict[str, Any]] = Field(None, description="agileCrmApi")

class AgilecrmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with agilecrm."""

    def __init__(self, credentials: Optional[AgilecrmCredentials] = None):
        """Initialize the agilecrm toolkit with optional credentials.

        Args:
            credentials: AgilecrmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all agilecrm tools with the configured credentials."""
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
        """Get all agilecrm tools with default credentials."""
        return get_agilecrm_tools()
