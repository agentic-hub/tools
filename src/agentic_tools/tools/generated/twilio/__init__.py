# twilio toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_twilio_tools() -> List[BaseTool]:
    """Get all twilio tools."""
    from . import operations
    return operations.get_tools()

class TwilioCredentials(BaseModel):
    """Credentials for twilio authentication."""
    twilio_api: Optional[Dict[str, Any]] = Field(None, description="twilioApi")

class TwilioToolkit(AgenticHubToolkit):
    """Toolkit for interacting with twilio."""

    def __init__(self, credentials: Optional[TwilioCredentials] = None):
        """Initialize the twilio toolkit with optional credentials.

        Args:
            credentials: TwilioCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all twilio tools with the configured credentials."""
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
        """Get all twilio tools with default credentials."""
        return get_twilio_tools()
