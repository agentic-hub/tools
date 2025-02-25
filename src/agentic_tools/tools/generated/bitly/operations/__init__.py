# bitly operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all bitly operation tools."""
    tools = []
    from .create import BitlyCreateTool
    tools.append(BitlyCreateTool())
    from .get import BitlyGetTool
    tools.append(BitlyGetTool())
    from .update import BitlyUpdateTool
    tools.append(BitlyUpdateTool())
    from .__custom_api_call__ import Bitly__custom_api_call__Tool
    tools.append(Bitly__custom_api_call__Tool())
    return tools
