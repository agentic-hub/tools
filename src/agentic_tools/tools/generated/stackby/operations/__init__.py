# stackby operations
from typing import List
from langchain.tools import BaseTool
from .. import StackbyCredentials

def get_tools() -> List[BaseTool]:
    """Get all stackby operation tools."""
    tools = []
    from .append import StackbyAppendTool
    tools.append(StackbyAppendTool())
    from .delete import StackbyDeleteTool
    tools.append(StackbyDeleteTool())
    from .list import StackbyListTool
    tools.append(StackbyListTool())
    from .read import StackbyReadTool
    tools.append(StackbyReadTool())
    return tools
