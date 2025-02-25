# pushbullet toolkit
from langchain.tools import BaseTool
from typing import List

def get_pushbullet_tools() -> List[BaseTool]:
    """Get all pushbullet tools."""
    from . import operations
    return operations.get_tools()

class PushbulletToolkit:
    """Toolkit for interacting with pushbullet."""

    def __init__(self):
        """Initialize the pushbullet toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all pushbullet tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all pushbullet tools with default credentials."""
        return get_pushbullet_tools()
