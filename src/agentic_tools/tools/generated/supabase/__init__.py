# supabase toolkit
from langchain.tools import BaseTool
from typing import List

def get_supabase_tools() -> List[BaseTool]:
    """Get all supabase tools."""
    from . import operations
    return operations.get_tools()

class SupabaseToolkit:
    """Toolkit for interacting with supabase."""

    def __init__(self):
        """Initialize the supabase toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all supabase tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all supabase tools with default credentials."""
        return get_supabase_tools()
