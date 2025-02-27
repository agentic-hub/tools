# questdb toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_questdb_tools() -> List[BaseTool]:
    """Get all questdb tools."""
    from . import operations
    return operations.get_tools()

class QuestdbCredentials(BaseModel):
    """Credentials for questdb authentication."""
    quest_db: Optional[Dict[str, Any]] = Field(None, description="questDb")

class QuestdbToolkit(AgenticHubToolkit):
    """Toolkit for interacting with questdb."""

    def __init__(self, credentials: Optional[QuestdbCredentials] = None):
        """Initialize the questdb toolkit with optional credentials.

        Args:
            credentials: QuestdbCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all questdb tools with the configured credentials."""
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
        """Get all questdb tools with default credentials."""
        return get_questdb_tools()
