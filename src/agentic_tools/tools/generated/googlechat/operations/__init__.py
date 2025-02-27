# googleChat operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GooglechatCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleChat operation tools."""
    tools = []
    from .get import GooglechatGetTool
    tools.append(GooglechatGetTool())
    from .getall import GooglechatGetallTool
    tools.append(GooglechatGetallTool())
    from .__custom_api_call__ import Googlechat__custom_api_call__Tool
    tools.append(Googlechat__custom_api_call__Tool())
    from .create import GooglechatCreateTool
    tools.append(GooglechatCreateTool())
    from .delete import GooglechatDeleteTool
    tools.append(GooglechatDeleteTool())
    from .get import GooglechatGetTool
    tools.append(GooglechatGetTool())
    from .update import GooglechatUpdateTool
    tools.append(GooglechatUpdateTool())
    from .__custom_api_call__ import Googlechat__custom_api_call__Tool
    tools.append(Googlechat__custom_api_call__Tool())
    from .get import GooglechatGetTool
    tools.append(GooglechatGetTool())
    from .getall import GooglechatGetallTool
    tools.append(GooglechatGetallTool())
    from .__custom_api_call__ import Googlechat__custom_api_call__Tool
    tools.append(Googlechat__custom_api_call__Tool())
    return tools
