# deepL operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all deepL operation tools."""
    tools = []
    from .translate import DeeplTranslateTool
    tools.append(DeeplTranslateTool())
    from .__custom_api_call__ import Deepl__custom_api_call__Tool
    tools.append(Deepl__custom_api_call__Tool())
    return tools
