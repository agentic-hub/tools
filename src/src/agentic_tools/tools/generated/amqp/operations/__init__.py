# amqp operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all amqp operation tools."""
    tools = []
    from .default import AmqpDefaultTool
    tools.append(AmqpDefaultTool())
    return tools
