# postHog operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all postHog operation tools."""
    tools = []
    from .create import PosthogCreateTool
    tools.append(PosthogCreateTool())
    from .create import PosthogCreateTool
    tools.append(PosthogCreateTool())
    from .create import PosthogCreateTool
    tools.append(PosthogCreateTool())
    from .page import PosthogPageTool
    tools.append(PosthogPageTool())
    from .screen import PosthogScreenTool
    tools.append(PosthogScreenTool())
    return tools
