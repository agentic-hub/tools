# mongodb toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mongodb_tools() -> List[BaseTool]:
    """Get all mongodb tools."""
    from . import operations
    return operations.get_tools()

class MongodbCredentials(BaseModel):
    """Credentials for mongodb authentication."""
    mongo_db: Optional[Dict[str, Any]] = Field(None, description="mongoDb")

class MongodbToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mongodb."""

    def __init__(self, credentials: Optional[MongodbCredentials] = None):
        """Initialize the mongodb toolkit with optional credentials.

        Args:
            credentials: MongodbCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mongodb tools with the configured credentials."""
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
        """Get all mongodb tools with default credentials."""
        return get_mongodb_tools()
