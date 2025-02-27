# elasticsearch toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_elasticsearch_tools() -> List[BaseTool]:
    """Get all elasticsearch tools."""
    from . import operations
    return operations.get_tools()

class ElasticsearchCredentials(BaseModel):
    """Credentials for elasticsearch authentication."""
    elasticsearch_api: Optional[Dict[str, Any]] = Field(None, description="elasticsearchApi")

class ElasticsearchToolkit(AgenticHubToolkit):
    """Toolkit for interacting with elasticsearch."""

    def __init__(self, credentials: Optional[ElasticsearchCredentials] = None):
        """Initialize the elasticsearch toolkit with optional credentials.

        Args:
            credentials: ElasticsearchCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all elasticsearch tools with the configured credentials."""
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
        """Get all elasticsearch tools with default credentials."""
        return get_elasticsearch_tools()
