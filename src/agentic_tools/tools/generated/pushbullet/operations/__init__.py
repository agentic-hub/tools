# pushbullet operations
from typing import List
from langchain.tools import BaseTool
from .. import PushbulletCredentials

def get_tools() -> List[BaseTool]:
    """Get all pushbullet operation tools."""
    tools = []
    from .create import PushbulletCreateTool
    tools.append(PushbulletCreateTool())
    from .delete import PushbulletDeleteTool
    tools.append(PushbulletDeleteTool())
    from .getall import PushbulletGetallTool
    tools.append(PushbulletGetallTool())
    from .update import PushbulletUpdateTool
    tools.append(PushbulletUpdateTool())
    from .__custom_api_call__ import Pushbullet__custom_api_call__Tool
    tools.append(Pushbullet__custom_api_call__Tool())
    return tools
