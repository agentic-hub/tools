# kafka operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import KafkaCredentials

def get_tools() -> List[BaseTool]:
    """Get all kafka operation tools."""
    tools = []
    from .default import KafkaDefaultTool
    tools.append(KafkaDefaultTool())
    return tools
