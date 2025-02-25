# gitlab operations
from typing import List
from langchain.tools import BaseTool
from .. import GitlabCredentials

def get_tools() -> List[BaseTool]:
    """Get all gitlab operation tools."""
    tools = []
    from .create import GitlabCreateTool
    tools.append(GitlabCreateTool())
    from .createcomment import GitlabCreatecommentTool
    tools.append(GitlabCreatecommentTool())
    from .edit import GitlabEditTool
    tools.append(GitlabEditTool())
    from .get import GitlabGetTool
    tools.append(GitlabGetTool())
    from .lock import GitlabLockTool
    tools.append(GitlabLockTool())
    from .__custom_api_call__ import Gitlab__custom_api_call__Tool
    tools.append(Gitlab__custom_api_call__Tool())
    from .get import GitlabGetTool
    tools.append(GitlabGetTool())
    from .getissues import GitlabGetissuesTool
    tools.append(GitlabGetissuesTool())
    from .__custom_api_call__ import Gitlab__custom_api_call__Tool
    tools.append(Gitlab__custom_api_call__Tool())
    from .getrepositories import GitlabGetrepositoriesTool
    tools.append(GitlabGetrepositoriesTool())
    from .__custom_api_call__ import Gitlab__custom_api_call__Tool
    tools.append(Gitlab__custom_api_call__Tool())
    from .create import GitlabCreateTool
    tools.append(GitlabCreateTool())
    from .delete import GitlabDeleteTool
    tools.append(GitlabDeleteTool())
    from .get import GitlabGetTool
    tools.append(GitlabGetTool())
    from .getall import GitlabGetallTool
    tools.append(GitlabGetallTool())
    from .update import GitlabUpdateTool
    tools.append(GitlabUpdateTool())
    from .__custom_api_call__ import Gitlab__custom_api_call__Tool
    tools.append(Gitlab__custom_api_call__Tool())
    from .create import GitlabCreateTool
    tools.append(GitlabCreateTool())
    from .delete import GitlabDeleteTool
    tools.append(GitlabDeleteTool())
    from .edit import GitlabEditTool
    tools.append(GitlabEditTool())
    from .get import GitlabGetTool
    tools.append(GitlabGetTool())
    from .list import GitlabListTool
    tools.append(GitlabListTool())
    from .__custom_api_call__ import Gitlab__custom_api_call__Tool
    tools.append(Gitlab__custom_api_call__Tool())
    return tools
