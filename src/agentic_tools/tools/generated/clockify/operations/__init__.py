# clockify operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ClockifyCredentials

def get_tools() -> List[BaseTool]:
    """Get all clockify operation tools."""
    tools = []
    from .create import ClockifyCreateTool
    tools.append(ClockifyCreateTool())
    from .delete import ClockifyDeleteTool
    tools.append(ClockifyDeleteTool())
    from .get import ClockifyGetTool
    tools.append(ClockifyGetTool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .update import ClockifyUpdateTool
    tools.append(ClockifyUpdateTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .create import ClockifyCreateTool
    tools.append(ClockifyCreateTool())
    from .delete import ClockifyDeleteTool
    tools.append(ClockifyDeleteTool())
    from .get import ClockifyGetTool
    tools.append(ClockifyGetTool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .update import ClockifyUpdateTool
    tools.append(ClockifyUpdateTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .create import ClockifyCreateTool
    tools.append(ClockifyCreateTool())
    from .delete import ClockifyDeleteTool
    tools.append(ClockifyDeleteTool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .update import ClockifyUpdateTool
    tools.append(ClockifyUpdateTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .create import ClockifyCreateTool
    tools.append(ClockifyCreateTool())
    from .delete import ClockifyDeleteTool
    tools.append(ClockifyDeleteTool())
    from .get import ClockifyGetTool
    tools.append(ClockifyGetTool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .update import ClockifyUpdateTool
    tools.append(ClockifyUpdateTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .create import ClockifyCreateTool
    tools.append(ClockifyCreateTool())
    from .delete import ClockifyDeleteTool
    tools.append(ClockifyDeleteTool())
    from .get import ClockifyGetTool
    tools.append(ClockifyGetTool())
    from .update import ClockifyUpdateTool
    tools.append(ClockifyUpdateTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    from .getall import ClockifyGetallTool
    tools.append(ClockifyGetallTool())
    from .__custom_api_call__ import Clockify__custom_api_call__Tool
    tools.append(Clockify__custom_api_call__Tool())
    return tools
