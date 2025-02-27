# discord operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import DiscordCredentials

def get_tools() -> List[BaseTool]:
    """Get all discord operation tools."""
    tools = []
    from .deletemessage import DiscordDeletemessageTool
    tools.append(DiscordDeletemessageTool())
    from .get import DiscordGetTool
    tools.append(DiscordGetTool())
    from .getall import DiscordGetallTool
    tools.append(DiscordGetallTool())
    from .react import DiscordReactTool
    tools.append(DiscordReactTool())
    from .send import DiscordSendTool
    tools.append(DiscordSendTool())
    from .__custom_api_call__ import Discord__custom_api_call__Tool
    tools.append(Discord__custom_api_call__Tool())
    from .create import DiscordCreateTool
    tools.append(DiscordCreateTool())
    from .deletechannel import DiscordDeletechannelTool
    tools.append(DiscordDeletechannelTool())
    from .get import DiscordGetTool
    tools.append(DiscordGetTool())
    from .getall import DiscordGetallTool
    tools.append(DiscordGetallTool())
    from .update import DiscordUpdateTool
    tools.append(DiscordUpdateTool())
    from .__custom_api_call__ import Discord__custom_api_call__Tool
    tools.append(Discord__custom_api_call__Tool())
    from .getall import DiscordGetallTool
    tools.append(DiscordGetallTool())
    from .roleadd import DiscordRoleaddTool
    tools.append(DiscordRoleaddTool())
    from .roleremove import DiscordRoleremoveTool
    tools.append(DiscordRoleremoveTool())
    from .__custom_api_call__ import Discord__custom_api_call__Tool
    tools.append(Discord__custom_api_call__Tool())
    from .sendlegacy import DiscordSendlegacyTool
    tools.append(DiscordSendlegacyTool())
    from .__custom_api_call__ import Discord__custom_api_call__Tool
    tools.append(Discord__custom_api_call__Tool())
    return tools
