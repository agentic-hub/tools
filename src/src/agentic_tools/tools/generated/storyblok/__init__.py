# storyblok toolkit
from langchain.tools import BaseTool
from typing import List

def get_storyblok_tools() -> List[BaseTool]:
    """Get all storyblok tools."""
    from . import operations
    return operations.get_tools()
