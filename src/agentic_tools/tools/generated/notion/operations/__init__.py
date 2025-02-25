# notion operations
from typing import List
from langchain.tools import BaseTool
from .. import NotionCredentials

def get_tools() -> List[BaseTool]:
    """Get all notion operation tools."""
    tools = []
    from .append import NotionAppendTool
    tools.append(NotionAppendTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    from .get import NotionGetTool
    tools.append(NotionGetTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    from .search import NotionSearchTool
    tools.append(NotionSearchTool())
    from .get import NotionGetTool
    tools.append(NotionGetTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    from .create import NotionCreateTool
    tools.append(NotionCreateTool())
    from .get import NotionGetTool
    tools.append(NotionGetTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    from .update import NotionUpdateTool
    tools.append(NotionUpdateTool())
    from .create import NotionCreateTool
    tools.append(NotionCreateTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    from .update import NotionUpdateTool
    tools.append(NotionUpdateTool())
    from .create import NotionCreateTool
    tools.append(NotionCreateTool())
    from .get import NotionGetTool
    tools.append(NotionGetTool())
    from .search import NotionSearchTool
    tools.append(NotionSearchTool())
    from .archive import NotionArchiveTool
    tools.append(NotionArchiveTool())
    from .create import NotionCreateTool
    tools.append(NotionCreateTool())
    from .search import NotionSearchTool
    tools.append(NotionSearchTool())
    from .get import NotionGetTool
    tools.append(NotionGetTool())
    from .getall import NotionGetallTool
    tools.append(NotionGetallTool())
    return tools
