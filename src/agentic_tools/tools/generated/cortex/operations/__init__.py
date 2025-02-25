# cortex operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all cortex operation tools."""
    tools = []
    from .execute import CortexExecuteTool
    tools.append(CortexExecuteTool())
    from .__custom_api_call__ import Cortex__custom_api_call__Tool
    tools.append(Cortex__custom_api_call__Tool())
    from .execute import CortexExecuteTool
    tools.append(CortexExecuteTool())
    from .__custom_api_call__ import Cortex__custom_api_call__Tool
    tools.append(Cortex__custom_api_call__Tool())
    from .get import CortexGetTool
    tools.append(CortexGetTool())
    from .report import CortexReportTool
    tools.append(CortexReportTool())
    from .__custom_api_call__ import Cortex__custom_api_call__Tool
    tools.append(Cortex__custom_api_call__Tool())
    return tools
