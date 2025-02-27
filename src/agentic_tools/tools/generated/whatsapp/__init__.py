# whatsapp toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_whatsapp_tools() -> List[BaseTool]:
    """Get all whatsapp tools."""
    from . import operations
    return operations.get_tools()

class WhatsappCredentials(BaseModel):
    """Credentials for whatsapp authentication."""
    whats_app_api: Optional[Dict[str, Any]] = Field(None, description="whatsAppApi")

class WhatsappToolkit(AgenticHubToolkit):
    """Toolkit for interacting with whatsapp."""

    def __init__(self, credentials: Optional[WhatsappCredentials] = None):
        """Initialize the whatsapp toolkit with optional credentials.

        Args:
            credentials: WhatsappCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all whatsapp tools with the configured credentials."""
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
        """Get all whatsapp tools with default credentials."""
        return get_whatsapp_tools()
