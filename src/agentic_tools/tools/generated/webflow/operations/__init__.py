# webflow operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all webflow operation tools."""
    tools = []
    from .create import WebflowCreateTool
    tools.append(WebflowCreateTool())
    from .delete import WebflowDeleteTool
    tools.append(WebflowDeleteTool())
    from .get import WebflowGetTool
    tools.append(WebflowGetTool())
    from .getall import WebflowGetallTool
    tools.append(WebflowGetallTool())
    from .update import WebflowUpdateTool
    tools.append(WebflowUpdateTool())
    from .__custom_api_call__ import Webflow__custom_api_call__Tool
    tools.append(Webflow__custom_api_call__Tool())
    return tools
