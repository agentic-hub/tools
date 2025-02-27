# strava operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import StravaCredentials

def get_tools() -> List[BaseTool]:
    """Get all strava operation tools."""
    tools = []
    from .create import StravaCreateTool
    tools.append(StravaCreateTool())
    from .get import StravaGetTool
    tools.append(StravaGetTool())
    from .getcomments import StravaGetcommentsTool
    tools.append(StravaGetcommentsTool())
    from .getkudos import StravaGetkudosTool
    tools.append(StravaGetkudosTool())
    from .getlaps import StravaGetlapsTool
    tools.append(StravaGetlapsTool())
    from .getall import StravaGetallTool
    tools.append(StravaGetallTool())
    from .getstreams import StravaGetstreamsTool
    tools.append(StravaGetstreamsTool())
    from .getzones import StravaGetzonesTool
    tools.append(StravaGetzonesTool())
    from .update import StravaUpdateTool
    tools.append(StravaUpdateTool())
    from .__custom_api_call__ import Strava__custom_api_call__Tool
    tools.append(Strava__custom_api_call__Tool())
    return tools
