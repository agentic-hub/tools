# pagerduty toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_pagerduty_tools() -> List[BaseTool]:
    """Get all pagerduty tools."""
    from . import operations
    return operations.get_tools()

class PagerdutyCredentials(BaseModel):
    """Credentials for pagerduty authentication."""
    pager_duty_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyApi")
    pager_duty_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyOAuth2Api")

class PagerdutyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with pagerduty."""

    def __init__(self, credentials: Optional[PagerdutyCredentials] = None):
        """Initialize the pagerduty toolkit with optional credentials.

        Args:
            credentials: PagerdutyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all pagerduty tools with the configured credentials."""
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
        """Get all pagerduty tools with default credentials."""
        return get_pagerduty_tools()
