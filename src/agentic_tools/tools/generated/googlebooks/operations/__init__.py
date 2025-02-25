# googleBooks operations
from typing import List
from langchain.tools import BaseTool
from .. import GooglebooksCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleBooks operation tools."""
    tools = []
    from .get import GooglebooksGetTool
    tools.append(GooglebooksGetTool())
    from .getall import GooglebooksGetallTool
    tools.append(GooglebooksGetallTool())
    from .__custom_api_call__ import Googlebooks__custom_api_call__Tool
    tools.append(Googlebooks__custom_api_call__Tool())
    from .add import GooglebooksAddTool
    tools.append(GooglebooksAddTool())
    from .clear import GooglebooksClearTool
    tools.append(GooglebooksClearTool())
    from .getall import GooglebooksGetallTool
    tools.append(GooglebooksGetallTool())
    from .move import GooglebooksMoveTool
    tools.append(GooglebooksMoveTool())
    from .remove import GooglebooksRemoveTool
    tools.append(GooglebooksRemoveTool())
    from .__custom_api_call__ import Googlebooks__custom_api_call__Tool
    tools.append(Googlebooks__custom_api_call__Tool())
    from .get import GooglebooksGetTool
    tools.append(GooglebooksGetTool())
    from .getall import GooglebooksGetallTool
    tools.append(GooglebooksGetallTool())
    from .__custom_api_call__ import Googlebooks__custom_api_call__Tool
    tools.append(Googlebooks__custom_api_call__Tool())
    return tools
