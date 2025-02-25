# storyblok toolkit
from langchain.tools import BaseTool
from typing import List

def get_storyblok_tools() -> List[BaseTool]:
    """Get all storyblok tools."""
    from . import operations
    return operations.get_tools()

class StoryblokToolkit:
    """Toolkit for interacting with storyblok."""

    def __init__(self):
        """Initialize the storyblok toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all storyblok tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all storyblok tools with default credentials."""
        return get_storyblok_tools()
