# mailjet operations
from typing import List
from langchain.tools import BaseTool
from .. import MailjetCredentials

def get_tools() -> List[BaseTool]:
    """Get all mailjet operation tools."""
    tools = []
    from .send import MailjetSendTool
    tools.append(MailjetSendTool())
    from .sendtemplate import MailjetSendtemplateTool
    tools.append(MailjetSendtemplateTool())
    from .__custom_api_call__ import Mailjet__custom_api_call__Tool
    tools.append(Mailjet__custom_api_call__Tool())
    from .send import MailjetSendTool
    tools.append(MailjetSendTool())
    from .__custom_api_call__ import Mailjet__custom_api_call__Tool
    tools.append(Mailjet__custom_api_call__Tool())
    return tools
