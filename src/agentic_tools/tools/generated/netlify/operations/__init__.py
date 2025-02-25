# netlify operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all netlify operation tools."""
    tools = []
    from .cancel import NetlifyCancelTool
    tools.append(NetlifyCancelTool())
    from .create import NetlifyCreateTool
    tools.append(NetlifyCreateTool())
    from .get import NetlifyGetTool
    tools.append(NetlifyGetTool())
    from .getall import NetlifyGetallTool
    tools.append(NetlifyGetallTool())
    from .delete import NetlifyDeleteTool
    tools.append(NetlifyDeleteTool())
    from .get import NetlifyGetTool
    tools.append(NetlifyGetTool())
    from .getall import NetlifyGetallTool
    tools.append(NetlifyGetallTool())
    return tools
