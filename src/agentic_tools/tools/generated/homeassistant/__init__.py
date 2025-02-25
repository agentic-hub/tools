# homeAssistant toolkit
from langchain.tools import BaseTool
from typing import List

def get_homeassistant_tools() -> List[BaseTool]:
    """Get all homeAssistant tools."""
    from . import operations
    return operations.get_tools()
