# github operations
from typing import List
from langchain.tools import BaseTool
from .. import GithubCredentials

def get_tools() -> List[BaseTool]:
    """Get all github operation tools."""
    tools = []
    from .getrepositories import GithubGetrepositoriesTool
    tools.append(GithubGetrepositoriesTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .create import GithubCreateTool
    tools.append(GithubCreateTool())
    from .createcomment import GithubCreatecommentTool
    tools.append(GithubCreatecommentTool())
    from .edit import GithubEditTool
    tools.append(GithubEditTool())
    from .get import GithubGetTool
    tools.append(GithubGetTool())
    from .lock import GithubLockTool
    tools.append(GithubLockTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .create import GithubCreateTool
    tools.append(GithubCreateTool())
    from .delete import GithubDeleteTool
    tools.append(GithubDeleteTool())
    from .edit import GithubEditTool
    tools.append(GithubEditTool())
    from .get import GithubGetTool
    tools.append(GithubGetTool())
    from .list import GithubListTool
    tools.append(GithubListTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .get import GithubGetTool
    tools.append(GithubGetTool())
    from .getissues import GithubGetissuesTool
    tools.append(GithubGetissuesTool())
    from .getlicense import GithubGetlicenseTool
    tools.append(GithubGetlicenseTool())
    from .getprofile import GithubGetprofileTool
    tools.append(GithubGetprofileTool())
    from .listpopularpaths import GithubListpopularpathsTool
    tools.append(GithubListpopularpathsTool())
    from .listreferrers import GithubListreferrersTool
    tools.append(GithubListreferrersTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .getrepositories import GithubGetrepositoriesTool
    tools.append(GithubGetrepositoriesTool())
    from .invite import GithubInviteTool
    tools.append(GithubInviteTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .create import GithubCreateTool
    tools.append(GithubCreateTool())
    from .delete import GithubDeleteTool
    tools.append(GithubDeleteTool())
    from .get import GithubGetTool
    tools.append(GithubGetTool())
    from .getall import GithubGetallTool
    tools.append(GithubGetallTool())
    from .update import GithubUpdateTool
    tools.append(GithubUpdateTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    from .create import GithubCreateTool
    tools.append(GithubCreateTool())
    from .get import GithubGetTool
    tools.append(GithubGetTool())
    from .getall import GithubGetallTool
    tools.append(GithubGetallTool())
    from .update import GithubUpdateTool
    tools.append(GithubUpdateTool())
    from .__custom_api_call__ import Github__custom_api_call__Tool
    tools.append(Github__custom_api_call__Tool())
    return tools
