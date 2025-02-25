# humanticAi operations
from typing import List
from langchain.tools import BaseTool
from .. import HumanticaiCredentials

def get_tools() -> List[BaseTool]:
    """Get all humanticAi operation tools."""
    tools = []
    from .create import HumanticaiCreateTool
    tools.append(HumanticaiCreateTool())
    from .get import HumanticaiGetTool
    tools.append(HumanticaiGetTool())
    from .update import HumanticaiUpdateTool
    tools.append(HumanticaiUpdateTool())
    return tools
