# rabbitmq operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import RabbitmqCredentials

def get_tools() -> List[BaseTool]:
    """Get all rabbitmq operation tools."""
    tools = []
    from .sendmessage import RabbitmqSendmessageTool
    tools.append(RabbitmqSendmessageTool())
    from .deletemessage import RabbitmqDeletemessageTool
    tools.append(RabbitmqDeletemessageTool())
    return tools
