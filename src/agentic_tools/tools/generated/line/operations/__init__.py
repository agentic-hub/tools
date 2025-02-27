# line operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import LineCredentials

def get_tools() -> List[BaseTool]:
    """Get all line operation tools."""
    tools = []
    from .send import LineSendTool
    tools.append(LineSendTool())
    from .__custom_api_call__ import Line__custom_api_call__Tool
    tools.append(Line__custom_api_call__Tool())
    return tools
