# elasticsecurity toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_elasticsecurity_tools() -> List[BaseTool]:
    """Get all elasticsecurity tools."""
    from . import operations
    return operations.get_tools()

class ElasticsecurityCredentials(BaseModel):
    """Credentials for elasticsecurity authentication."""
    elastic_security_api: Optional[Dict[str, Any]] = Field(None, description="elasticSecurityApi")

class ElasticsecurityToolkit(AgenticHubToolkit):
    """Toolkit for interacting with elasticsecurity."""

    def __init__(self, credentials: Optional[ElasticsecurityCredentials] = None):
        """Initialize the elasticsecurity toolkit with optional credentials.

        Args:
            credentials: ElasticsecurityCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all elasticsecurity tools with the configured credentials."""
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
        """Get all elasticsecurity tools with default credentials."""
        return get_elasticsecurity_tools()
