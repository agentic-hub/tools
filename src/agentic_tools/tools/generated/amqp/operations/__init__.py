# amqp operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import AmqpCredentials

def get_tools() -> List[BaseTool]:
    """Get all amqp operation tools."""
    tools = []
    from .default import AmqpDefaultTool
    tools.append(AmqpDefaultTool())
    return tools
