# storyblok toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_storyblok_tools() -> List[BaseTool]:
    """Get all storyblok tools."""
    from . import operations
    return operations.get_tools()

class StoryblokCredentials(BaseModel):
    """Credentials for storyblok authentication."""
    storyblok_content_api: Optional[Dict[str, Any]] = Field(None, description="storyblokContentApi")
    storyblok_management_api: Optional[Dict[str, Any]] = Field(None, description="storyblokManagementApi")

class StoryblokToolkit(AgenticHubToolkit):
    """Toolkit for interacting with storyblok."""

    def __init__(self, credentials: Optional[StoryblokCredentials] = None):
        """Initialize the storyblok toolkit with optional credentials.

        Args:
            credentials: StoryblokCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all storyblok tools with the configured credentials."""
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
        """Get all storyblok tools with default credentials."""
        return get_storyblok_tools()
