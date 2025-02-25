# sendInBlue operations
from typing import List
from langchain.tools import BaseTool
from .. import SendinblueCredentials

def get_tools() -> List[BaseTool]:
    """Get all sendInBlue operation tools."""
    tools = []
    from .create import SendinblueCreateTool
    tools.append(SendinblueCreateTool())
    from .update import SendinblueUpdateTool
    tools.append(SendinblueUpdateTool())
    from .delete import SendinblueDeleteTool
    tools.append(SendinblueDeleteTool())
    from .getall import SendinblueGetallTool
    tools.append(SendinblueGetallTool())
    from .__custom_api_call__ import Sendinblue__custom_api_call__Tool
    tools.append(Sendinblue__custom_api_call__Tool())
    from .create import SendinblueCreateTool
    tools.append(SendinblueCreateTool())
    from .delete import SendinblueDeleteTool
    tools.append(SendinblueDeleteTool())
    from .getall import SendinblueGetallTool
    tools.append(SendinblueGetallTool())
    from .__custom_api_call__ import Sendinblue__custom_api_call__Tool
    tools.append(Sendinblue__custom_api_call__Tool())
    from .create import SendinblueCreateTool
    tools.append(SendinblueCreateTool())
    from .upsert import SendinblueUpsertTool
    tools.append(SendinblueUpsertTool())
    from .delete import SendinblueDeleteTool
    tools.append(SendinblueDeleteTool())
    from .get import SendinblueGetTool
    tools.append(SendinblueGetTool())
    from .getall import SendinblueGetallTool
    tools.append(SendinblueGetallTool())
    from .update import SendinblueUpdateTool
    tools.append(SendinblueUpdateTool())
    from .__custom_api_call__ import Sendinblue__custom_api_call__Tool
    tools.append(Sendinblue__custom_api_call__Tool())
    from .send import SendinblueSendTool
    tools.append(SendinblueSendTool())
    from .sendtemplate import SendinblueSendtemplateTool
    tools.append(SendinblueSendtemplateTool())
    from .__custom_api_call__ import Sendinblue__custom_api_call__Tool
    tools.append(Sendinblue__custom_api_call__Tool())
    return tools
