# telegramTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all telegramTrigger operation tools."""
    tools = []
    from .default import TelegramtriggerDefaultTool
    tools.append(TelegramtriggerDefaultTool())
    return tools
