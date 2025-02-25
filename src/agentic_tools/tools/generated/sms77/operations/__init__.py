# sms77 operations
from typing import List
from langchain.tools import BaseTool
from .. import Sms77Credentials

def get_tools() -> List[BaseTool]:
    """Get all sms77 operation tools."""
    tools = []
    from .send import Sms77SendTool
    tools.append(Sms77SendTool())
    from .__custom_api_call__ import Sms77__custom_api_call__Tool
    tools.append(Sms77__custom_api_call__Tool())
    from .send import Sms77SendTool
    tools.append(Sms77SendTool())
    from .__custom_api_call__ import Sms77__custom_api_call__Tool
    tools.append(Sms77__custom_api_call__Tool())
    return tools
