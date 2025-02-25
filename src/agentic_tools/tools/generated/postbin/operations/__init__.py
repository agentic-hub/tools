# postBin operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all postBin operation tools."""
    tools = []
    from .create import PostbinCreateTool
    tools.append(PostbinCreateTool())
    from .get import PostbinGetTool
    tools.append(PostbinGetTool())
    from .delete import PostbinDeleteTool
    tools.append(PostbinDeleteTool())
    from .get import PostbinGetTool
    tools.append(PostbinGetTool())
    from .removefirst import PostbinRemovefirstTool
    tools.append(PostbinRemovefirstTool())
    from .send import PostbinSendTool
    tools.append(PostbinSendTool())
    return tools
