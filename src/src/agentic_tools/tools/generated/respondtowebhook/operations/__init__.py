# respondToWebhook operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all respondToWebhook operation tools."""
    tools = []
    from .default import RespondtowebhookDefaultTool
    tools.append(RespondtowebhookDefaultTool())
    return tools
