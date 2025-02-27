# jenkins operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import JenkinsCredentials

def get_tools() -> List[BaseTool]:
    """Get all jenkins operation tools."""
    tools = []
    from .copy import JenkinsCopyTool
    tools.append(JenkinsCopyTool())
    from .create import JenkinsCreateTool
    tools.append(JenkinsCreateTool())
    from .trigger import JenkinsTriggerTool
    tools.append(JenkinsTriggerTool())
    from .triggerparams import JenkinsTriggerparamsTool
    tools.append(JenkinsTriggerparamsTool())
    from .cancelquietdown import JenkinsCancelquietdownTool
    tools.append(JenkinsCancelquietdownTool())
    from .quietdown import JenkinsQuietdownTool
    tools.append(JenkinsQuietdownTool())
    from .restart import JenkinsRestartTool
    tools.append(JenkinsRestartTool())
    from .saferestart import JenkinsSaferestartTool
    tools.append(JenkinsSaferestartTool())
    from .safeexit import JenkinsSafeexitTool
    tools.append(JenkinsSafeexitTool())
    from .exit import JenkinsExitTool
    tools.append(JenkinsExitTool())
    from .getall import JenkinsGetallTool
    tools.append(JenkinsGetallTool())
    return tools
