# activecampaign toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_activecampaign_tools() -> List[BaseTool]:
    """Get all activecampaign tools."""
    from . import operations
    return operations.get_tools()

class ActivecampaignCredentials(BaseModel):
    """Credentials for activecampaign authentication."""
    active_campaign_api: Optional[Dict[str, Any]] = Field(None, description="activeCampaignApi")

class ActivecampaignToolkit(AgenticHubToolkit):
    """Toolkit for interacting with activecampaign."""

    def __init__(self, credentials: Optional[ActivecampaignCredentials] = None):
        """Initialize the activecampaign toolkit with optional credentials.

        Args:
            credentials: ActivecampaignCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all activecampaign tools with the configured credentials."""
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
        """Get all activecampaign tools with default credentials."""
        return get_activecampaign_tools()
