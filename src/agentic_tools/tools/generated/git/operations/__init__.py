# git operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GitCredentials

def get_tools() -> List[BaseTool]:
    """Get all git operation tools."""
    tools = []
    from .add import GitAddTool
    tools.append(GitAddTool())
    from .addconfig import GitAddconfigTool
    tools.append(GitAddconfigTool())
    from .clone import GitCloneTool
    tools.append(GitCloneTool())
    from .commit import GitCommitTool
    tools.append(GitCommitTool())
    from .fetch import GitFetchTool
    tools.append(GitFetchTool())
    from .listconfig import GitListconfigTool
    tools.append(GitListconfigTool())
    from .log import GitLogTool
    tools.append(GitLogTool())
    from .pull import GitPullTool
    tools.append(GitPullTool())
    from .push import GitPushTool
    tools.append(GitPushTool())
    from .pushtags import GitPushtagsTool
    tools.append(GitPushtagsTool())
    from .status import GitStatusTool
    tools.append(GitStatusTool())
    from .tag import GitTagTool
    tools.append(GitTagTool())
    from .usersetup import GitUsersetupTool
    tools.append(GitUsersetupTool())
    return tools
