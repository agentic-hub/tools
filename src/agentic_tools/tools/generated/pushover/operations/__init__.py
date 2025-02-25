# pushover operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all pushover operation tools."""
    tools = []
    from .push import PushoverPushTool
    tools.append(PushoverPushTool())
    from .__custom_api_call__ import Pushover__custom_api_call__Tool
    tools.append(Pushover__custom_api_call__Tool())
    return tools
