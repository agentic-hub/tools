# twilio operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all twilio operation tools."""
    tools = []
    from .send import TwilioSendTool
    tools.append(TwilioSendTool())
    from .__custom_api_call__ import Twilio__custom_api_call__Tool
    tools.append(Twilio__custom_api_call__Tool())
    from .make import TwilioMakeTool
    tools.append(TwilioMakeTool())
    from .__custom_api_call__ import Twilio__custom_api_call__Tool
    tools.append(Twilio__custom_api_call__Tool())
    return tools
