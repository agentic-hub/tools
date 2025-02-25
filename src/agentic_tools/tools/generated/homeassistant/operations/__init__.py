# homeAssistant operations
from typing import List
from langchain.tools import BaseTool
from .. import HomeassistantCredentials

def get_tools() -> List[BaseTool]:
    """Get all homeAssistant operation tools."""
    tools = []
    from .getscreenshot import HomeassistantGetscreenshotTool
    tools.append(HomeassistantGetscreenshotTool())
    from .get import HomeassistantGetTool
    tools.append(HomeassistantGetTool())
    from .check import HomeassistantCheckTool
    tools.append(HomeassistantCheckTool())
    from .create import HomeassistantCreateTool
    tools.append(HomeassistantCreateTool())
    from .getall import HomeassistantGetallTool
    tools.append(HomeassistantGetallTool())
    from .getall import HomeassistantGetallTool
    tools.append(HomeassistantGetallTool())
    from .geterrologs import HomeassistantGeterrologsTool
    tools.append(HomeassistantGeterrologsTool())
    from .getlogbookentries import HomeassistantGetlogbookentriesTool
    tools.append(HomeassistantGetlogbookentriesTool())
    from .call import HomeassistantCallTool
    tools.append(HomeassistantCallTool())
    from .getall import HomeassistantGetallTool
    tools.append(HomeassistantGetallTool())
    from .upsert import HomeassistantUpsertTool
    tools.append(HomeassistantUpsertTool())
    from .get import HomeassistantGetTool
    tools.append(HomeassistantGetTool())
    from .getall import HomeassistantGetallTool
    tools.append(HomeassistantGetallTool())
    from .create import HomeassistantCreateTool
    tools.append(HomeassistantCreateTool())
    return tools
