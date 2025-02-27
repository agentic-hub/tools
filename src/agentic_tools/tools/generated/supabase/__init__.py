# supabase toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_supabase_tools() -> List[BaseTool]:
    """Get all supabase tools."""
    from . import operations
    return operations.get_tools()

class SupabaseCredentials(BaseModel):
    """Credentials for supabase authentication."""
    supabase_api: Optional[Dict[str, Any]] = Field(None, description="supabaseApi")

class SupabaseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with supabase."""

    def __init__(self, credentials: Optional[SupabaseCredentials] = None):
        """Initialize the supabase toolkit with optional credentials.

        Args:
            credentials: SupabaseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all supabase tools with the configured credentials."""
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
        """Get all supabase tools with default credentials."""
        return get_supabase_tools()
