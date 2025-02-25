# twake operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all twake operation tools."""
    tools = []
    from .send import TwakeSendTool
    tools.append(TwakeSendTool())
    from .__custom_api_call__ import Twake__custom_api_call__Tool
    tools.append(Twake__custom_api_call__Tool())
    return tools
