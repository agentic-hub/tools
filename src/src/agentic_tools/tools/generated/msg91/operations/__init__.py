# msg91 operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all msg91 operation tools."""
    tools = []
    from .send import Msg91SendTool
    tools.append(Msg91SendTool())
    return tools
