# googletranslate toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googletranslate_tools() -> List[BaseTool]:
    """Get all googletranslate tools."""
    from . import operations
    return operations.get_tools()

class GoogletranslateCredentials(BaseModel):
    """Credentials for googletranslate authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_translate_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleTranslateOAuth2Api")

class GoogletranslateToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googletranslate."""

    def __init__(self, credentials: Optional[GoogletranslateCredentials] = None):
        """Initialize the googletranslate toolkit with optional credentials.

        Args:
            credentials: GoogletranslateCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googletranslate tools with the configured credentials."""
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
        """Get all googletranslate tools with default credentials."""
        return get_googletranslate_tools()
