# gotify operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GotifyCredentials

def get_tools() -> List[BaseTool]:
    """Get all gotify operation tools."""
    tools = []
    from .create import GotifyCreateTool
    tools.append(GotifyCreateTool())
    from .delete import GotifyDeleteTool
    tools.append(GotifyDeleteTool())
    from .getall import GotifyGetallTool
    tools.append(GotifyGetallTool())
    return tools
