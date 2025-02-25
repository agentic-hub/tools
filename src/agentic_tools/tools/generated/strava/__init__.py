# strava toolkit
from langchain.tools import BaseTool
from typing import List

def get_strava_tools() -> List[BaseTool]:
    """Get all strava tools."""
    from . import operations
    return operations.get_tools()
