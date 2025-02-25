# filemaker operations
from typing import List
from langchain.tools import BaseTool
from .. import FilemakerCredentials

def get_tools() -> List[BaseTool]:
    """Get all filemaker operation tools."""
    tools = []
    from .default import FilemakerDefaultTool
    tools.append(FilemakerDefaultTool())
    return tools
