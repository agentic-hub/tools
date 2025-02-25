# mailerLiteTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mailerLiteTrigger operation tools."""
    tools = []
    from .default import MailerlitetriggerDefaultTool
    tools.append(MailerlitetriggerDefaultTool())
    return tools
