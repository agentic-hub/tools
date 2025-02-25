# vonage operations
from typing import List
from langchain.tools import BaseTool
from .. import VonageCredentials

def get_tools() -> List[BaseTool]:
    """Get all vonage operation tools."""
    tools = []
    from .send import VonageSendTool
    tools.append(VonageSendTool())
    return tools
