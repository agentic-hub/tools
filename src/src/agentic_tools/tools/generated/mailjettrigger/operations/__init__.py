# mailjetTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mailjetTrigger operation tools."""
    tools = []
    from .default import MailjettriggerDefaultTool
    tools.append(MailjettriggerDefaultTool())
    return tools
