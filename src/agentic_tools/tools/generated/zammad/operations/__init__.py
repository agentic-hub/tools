# zammad operations
from typing import List
from langchain.tools import BaseTool
from .. import ZammadCredentials

def get_tools() -> List[BaseTool]:
    """Get all zammad operation tools."""
    tools = []
    from .create import ZammadCreateTool
    tools.append(ZammadCreateTool())
    from .delete import ZammadDeleteTool
    tools.append(ZammadDeleteTool())
    from .get import ZammadGetTool
    tools.append(ZammadGetTool())
    from .getall import ZammadGetallTool
    tools.append(ZammadGetallTool())
    from .update import ZammadUpdateTool
    tools.append(ZammadUpdateTool())
    from .create import ZammadCreateTool
    tools.append(ZammadCreateTool())
    from .delete import ZammadDeleteTool
    tools.append(ZammadDeleteTool())
    from .get import ZammadGetTool
    tools.append(ZammadGetTool())
    from .getall import ZammadGetallTool
    tools.append(ZammadGetallTool())
    from .update import ZammadUpdateTool
    tools.append(ZammadUpdateTool())
    from .create import ZammadCreateTool
    tools.append(ZammadCreateTool())
    from .delete import ZammadDeleteTool
    tools.append(ZammadDeleteTool())
    from .get import ZammadGetTool
    tools.append(ZammadGetTool())
    from .getall import ZammadGetallTool
    tools.append(ZammadGetallTool())
    from .create import ZammadCreateTool
    tools.append(ZammadCreateTool())
    from .delete import ZammadDeleteTool
    tools.append(ZammadDeleteTool())
    from .get import ZammadGetTool
    tools.append(ZammadGetTool())
    from .getall import ZammadGetallTool
    tools.append(ZammadGetallTool())
    from .getself import ZammadGetselfTool
    tools.append(ZammadGetselfTool())
    from .update import ZammadUpdateTool
    tools.append(ZammadUpdateTool())
    return tools
