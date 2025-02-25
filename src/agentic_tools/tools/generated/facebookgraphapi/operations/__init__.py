# facebookGraphApi operations
from typing import List
from langchain.tools import BaseTool
from .. import FacebookgraphapiCredentials

def get_tools() -> List[BaseTool]:
    """Get all facebookGraphApi operation tools."""
    tools = []
    from .default import FacebookgraphapiDefaultTool
    tools.append(FacebookgraphapiDefaultTool())
    return tools
