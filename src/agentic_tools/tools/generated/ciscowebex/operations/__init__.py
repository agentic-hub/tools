# ciscoWebex operations
from typing import List
from langchain.tools import BaseTool
from .. import CiscowebexCredentials

def get_tools() -> List[BaseTool]:
    """Get all ciscoWebex operation tools."""
    tools = []
    from .create import CiscowebexCreateTool
    tools.append(CiscowebexCreateTool())
    from .delete import CiscowebexDeleteTool
    tools.append(CiscowebexDeleteTool())
    from .get import CiscowebexGetTool
    tools.append(CiscowebexGetTool())
    from .getall import CiscowebexGetallTool
    tools.append(CiscowebexGetallTool())
    from .update import CiscowebexUpdateTool
    tools.append(CiscowebexUpdateTool())
    from .__custom_api_call__ import Ciscowebex__custom_api_call__Tool
    tools.append(Ciscowebex__custom_api_call__Tool())
    from .create import CiscowebexCreateTool
    tools.append(CiscowebexCreateTool())
    from .delete import CiscowebexDeleteTool
    tools.append(CiscowebexDeleteTool())
    from .get import CiscowebexGetTool
    tools.append(CiscowebexGetTool())
    from .getall import CiscowebexGetallTool
    tools.append(CiscowebexGetallTool())
    from .update import CiscowebexUpdateTool
    tools.append(CiscowebexUpdateTool())
    from .__custom_api_call__ import Ciscowebex__custom_api_call__Tool
    tools.append(Ciscowebex__custom_api_call__Tool())
    return tools
