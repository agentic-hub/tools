# webhook operations
from typing import List
from langchain.tools import BaseTool
from .. import WebhookCredentials

def get_tools() -> List[BaseTool]:
    """Get all webhook operation tools."""
    tools = []
    from .default import WebhookDefaultTool
    tools.append(WebhookDefaultTool())
    return tools
