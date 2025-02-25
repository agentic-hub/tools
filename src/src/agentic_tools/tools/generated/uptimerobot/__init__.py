# uptimeRobot toolkit
from langchain.tools import BaseTool
from typing import List

def get_uptimerobot_tools() -> List[BaseTool]:
    """Get all uptimeRobot tools."""
    from . import operations
    return operations.get_tools()
