# awsSqs operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsSqs operation tools."""
    tools = []
    from .sendmessage import AwssqsSendmessageTool
    tools.append(AwssqsSendmessageTool())
    from .__custom_api_call__ import Awssqs__custom_api_call__Tool
    tools.append(Awssqs__custom_api_call__Tool())
    return tools
