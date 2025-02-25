# mailchimpTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mailchimpTrigger operation tools."""
    tools = []
    from .default import MailchimptriggerDefaultTool
    tools.append(MailchimptriggerDefaultTool())
    return tools
