# respondToWebhook operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all respondToWebhook operation tools."""
    tools = []
    from .default import RespondtowebhookDefaultTool
    tools.append(RespondtowebhookDefaultTool())
    return tools
