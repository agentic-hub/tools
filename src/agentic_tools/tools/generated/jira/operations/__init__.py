# jira operations
from typing import List
from langchain.tools import BaseTool
from .. import JiraCredentials

def get_tools() -> List[BaseTool]:
    """Get all jira operation tools."""
    tools = []
    from .changelog import JiraChangelogTool
    tools.append(JiraChangelogTool())
    from .create import JiraCreateTool
    tools.append(JiraCreateTool())
    from .delete import JiraDeleteTool
    tools.append(JiraDeleteTool())
    from .get import JiraGetTool
    tools.append(JiraGetTool())
    from .getall import JiraGetallTool
    tools.append(JiraGetallTool())
    from .notify import JiraNotifyTool
    tools.append(JiraNotifyTool())
    from .transitions import JiraTransitionsTool
    tools.append(JiraTransitionsTool())
    from .update import JiraUpdateTool
    tools.append(JiraUpdateTool())
    from .__custom_api_call__ import Jira__custom_api_call__Tool
    tools.append(Jira__custom_api_call__Tool())
    from .add import JiraAddTool
    tools.append(JiraAddTool())
    from .get import JiraGetTool
    tools.append(JiraGetTool())
    from .getall import JiraGetallTool
    tools.append(JiraGetallTool())
    from .remove import JiraRemoveTool
    tools.append(JiraRemoveTool())
    from .__custom_api_call__ import Jira__custom_api_call__Tool
    tools.append(Jira__custom_api_call__Tool())
    from .add import JiraAddTool
    tools.append(JiraAddTool())
    from .get import JiraGetTool
    tools.append(JiraGetTool())
    from .getall import JiraGetallTool
    tools.append(JiraGetallTool())
    from .remove import JiraRemoveTool
    tools.append(JiraRemoveTool())
    from .update import JiraUpdateTool
    tools.append(JiraUpdateTool())
    from .__custom_api_call__ import Jira__custom_api_call__Tool
    tools.append(Jira__custom_api_call__Tool())
    from .create import JiraCreateTool
    tools.append(JiraCreateTool())
    from .delete import JiraDeleteTool
    tools.append(JiraDeleteTool())
    from .get import JiraGetTool
    tools.append(JiraGetTool())
    from .__custom_api_call__ import Jira__custom_api_call__Tool
    tools.append(Jira__custom_api_call__Tool())
    return tools
