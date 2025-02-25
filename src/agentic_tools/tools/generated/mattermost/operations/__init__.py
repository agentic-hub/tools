# mattermost operations
from typing import List
from langchain.tools import BaseTool
from .. import MattermostCredentials

def get_tools() -> List[BaseTool]:
    """Get all mattermost operation tools."""
    tools = []
    from .adduser import MattermostAdduserTool
    tools.append(MattermostAdduserTool())
    from .create import MattermostCreateTool
    tools.append(MattermostCreateTool())
    from .delete import MattermostDeleteTool
    tools.append(MattermostDeleteTool())
    from .members import MattermostMembersTool
    tools.append(MattermostMembersTool())
    from .restore import MattermostRestoreTool
    tools.append(MattermostRestoreTool())
    from .search import MattermostSearchTool
    tools.append(MattermostSearchTool())
    from .statistics import MattermostStatisticsTool
    tools.append(MattermostStatisticsTool())
    from .__custom_api_call__ import Mattermost__custom_api_call__Tool
    tools.append(Mattermost__custom_api_call__Tool())
    from .delete import MattermostDeleteTool
    tools.append(MattermostDeleteTool())
    from .post import MattermostPostTool
    tools.append(MattermostPostTool())
    from .postephemeral import MattermostPostephemeralTool
    tools.append(MattermostPostephemeralTool())
    from .__custom_api_call__ import Mattermost__custom_api_call__Tool
    tools.append(Mattermost__custom_api_call__Tool())
    from .create import MattermostCreateTool
    tools.append(MattermostCreateTool())
    from .delete import MattermostDeleteTool
    tools.append(MattermostDeleteTool())
    from .getall import MattermostGetallTool
    tools.append(MattermostGetallTool())
    from .__custom_api_call__ import Mattermost__custom_api_call__Tool
    tools.append(Mattermost__custom_api_call__Tool())
    from .create import MattermostCreateTool
    tools.append(MattermostCreateTool())
    from .deactive import MattermostDeactiveTool
    tools.append(MattermostDeactiveTool())
    from .getbyemail import MattermostGetbyemailTool
    tools.append(MattermostGetbyemailTool())
    from .getbyid import MattermostGetbyidTool
    tools.append(MattermostGetbyidTool())
    from .getall import MattermostGetallTool
    tools.append(MattermostGetallTool())
    from .invite import MattermostInviteTool
    tools.append(MattermostInviteTool())
    from .__custom_api_call__ import Mattermost__custom_api_call__Tool
    tools.append(Mattermost__custom_api_call__Tool())
    return tools
