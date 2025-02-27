# gSuiteAdmin operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GsuiteadminCredentials

def get_tools() -> List[BaseTool]:
    """Get all gSuiteAdmin operation tools."""
    tools = []
    from .create import GsuiteadminCreateTool
    tools.append(GsuiteadminCreateTool())
    from .delete import GsuiteadminDeleteTool
    tools.append(GsuiteadminDeleteTool())
    from .get import GsuiteadminGetTool
    tools.append(GsuiteadminGetTool())
    from .getall import GsuiteadminGetallTool
    tools.append(GsuiteadminGetallTool())
    from .update import GsuiteadminUpdateTool
    tools.append(GsuiteadminUpdateTool())
    from .__custom_api_call__ import Gsuiteadmin__custom_api_call__Tool
    tools.append(Gsuiteadmin__custom_api_call__Tool())
    from .create import GsuiteadminCreateTool
    tools.append(GsuiteadminCreateTool())
    from .delete import GsuiteadminDeleteTool
    tools.append(GsuiteadminDeleteTool())
    from .get import GsuiteadminGetTool
    tools.append(GsuiteadminGetTool())
    from .getall import GsuiteadminGetallTool
    tools.append(GsuiteadminGetallTool())
    from .update import GsuiteadminUpdateTool
    tools.append(GsuiteadminUpdateTool())
    from .__custom_api_call__ import Gsuiteadmin__custom_api_call__Tool
    tools.append(Gsuiteadmin__custom_api_call__Tool())
    return tools
