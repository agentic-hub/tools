# npm operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all npm operation tools."""
    tools = []
    from .getmetadata import NpmGetmetadataTool
    tools.append(NpmGetmetadataTool())
    from .getversions import NpmGetversionsTool
    tools.append(NpmGetversionsTool())
    from .search import NpmSearchTool
    tools.append(NpmSearchTool())
    from .__custom_api_call__ import Npm__custom_api_call__Tool
    tools.append(Npm__custom_api_call__Tool())
    from .getmany import NpmGetmanyTool
    tools.append(NpmGetmanyTool())
    from .update import NpmUpdateTool
    tools.append(NpmUpdateTool())
    from .__custom_api_call__ import Npm__custom_api_call__Tool
    tools.append(Npm__custom_api_call__Tool())
    return tools
