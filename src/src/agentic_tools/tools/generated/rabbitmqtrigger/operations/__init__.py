# rabbitmqTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all rabbitmqTrigger operation tools."""
    tools = []
    from .default import RabbitmqtriggerDefaultTool
    tools.append(RabbitmqtriggerDefaultTool())
    return tools
