# cron toolkit
from langchain.tools import BaseTool
from typing import List

def get_cron_tools() -> List[BaseTool]:
    """Get all cron tools."""
    from . import operations
    return operations.get_tools()

class CronToolkit:
    """Toolkit for interacting with cron."""

    def __init__(self):
        """Initialize the cron toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all cron tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all cron tools with default credentials."""
        return get_cron_tools()
