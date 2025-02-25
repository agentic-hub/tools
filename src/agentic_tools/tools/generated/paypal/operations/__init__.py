# payPal operations
from typing import List
from langchain.tools import BaseTool
from .. import PaypalCredentials

def get_tools() -> List[BaseTool]:
    """Get all payPal operation tools."""
    tools = []
    from .create import PaypalCreateTool
    tools.append(PaypalCreateTool())
    from .get import PaypalGetTool
    tools.append(PaypalGetTool())
    from .cancel import PaypalCancelTool
    tools.append(PaypalCancelTool())
    from .get import PaypalGetTool
    tools.append(PaypalGetTool())
    return tools
