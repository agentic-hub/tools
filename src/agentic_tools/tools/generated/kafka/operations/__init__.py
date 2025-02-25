# kafka operations
from typing import List
from langchain.tools import BaseTool
from .. import KafkaCredentials

def get_tools() -> List[BaseTool]:
    """Get all kafka operation tools."""
    tools = []
    from .default import KafkaDefaultTool
    tools.append(KafkaDefaultTool())
    return tools
