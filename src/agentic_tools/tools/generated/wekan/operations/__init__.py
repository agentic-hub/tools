# wekan operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import WekanCredentials

def get_tools() -> List[BaseTool]:
    """Get all wekan operation tools."""
    tools = []
    from .create import WekanCreateTool
    tools.append(WekanCreateTool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .getall import WekanGetallTool
    tools.append(WekanGetallTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    from .create import WekanCreateTool
    tools.append(WekanCreateTool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .getall import WekanGetallTool
    tools.append(WekanGetallTool())
    from .update import WekanUpdateTool
    tools.append(WekanUpdateTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    from .create import WekanCreateTool
    tools.append(WekanCreateTool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .getall import WekanGetallTool
    tools.append(WekanGetallTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    from .create import WekanCreateTool
    tools.append(WekanCreateTool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .getall import WekanGetallTool
    tools.append(WekanGetallTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .update import WekanUpdateTool
    tools.append(WekanUpdateTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    from .create import WekanCreateTool
    tools.append(WekanCreateTool())
    from .delete import WekanDeleteTool
    tools.append(WekanDeleteTool())
    from .get import WekanGetTool
    tools.append(WekanGetTool())
    from .getall import WekanGetallTool
    tools.append(WekanGetallTool())
    from .__custom_api_call__ import Wekan__custom_api_call__Tool
    tools.append(Wekan__custom_api_call__Tool())
    return tools
