# whatsApp operations
from typing import List
from langchain.tools import BaseTool
from .. import WhatsappCredentials

def get_tools() -> List[BaseTool]:
    """Get all whatsApp operation tools."""
    tools = []
    from .send import WhatsappSendTool
    tools.append(WhatsappSendTool())
    from .sendtemplate import WhatsappSendtemplateTool
    tools.append(WhatsappSendtemplateTool())
    from .__custom_api_call__ import Whatsapp__custom_api_call__Tool
    tools.append(Whatsapp__custom_api_call__Tool())
    from .mediaupload import WhatsappMediauploadTool
    tools.append(WhatsappMediauploadTool())
    from .mediaurlget import WhatsappMediaurlgetTool
    tools.append(WhatsappMediaurlgetTool())
    from .mediadelete import WhatsappMediadeleteTool
    tools.append(WhatsappMediadeleteTool())
    from .__custom_api_call__ import Whatsapp__custom_api_call__Tool
    tools.append(Whatsapp__custom_api_call__Tool())
    return tools
