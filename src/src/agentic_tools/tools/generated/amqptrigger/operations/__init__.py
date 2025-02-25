# amqpTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all amqpTrigger operation tools."""
    tools = []
    from .default import AmqptriggerDefaultTool
    tools.append(AmqptriggerDefaultTool())
    return tools
