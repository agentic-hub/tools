# facebookGraphApi operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import FacebookgraphapiCredentials

def get_tools() -> List[BaseTool]:
    """Get all facebookGraphApi operation tools."""
    tools = []
    from .default import FacebookgraphapiDefaultTool
    tools.append(FacebookgraphapiDefaultTool())
    return tools
