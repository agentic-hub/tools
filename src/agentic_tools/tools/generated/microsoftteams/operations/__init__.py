# microsoftTeams operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MicrosoftteamsCredentials

def get_tools() -> List[BaseTool]:
    """Get all microsoftTeams operation tools."""
    tools = []
    from .create import MicrosoftteamsCreateTool
    tools.append(MicrosoftteamsCreateTool())
    from .deletechannel import MicrosoftteamsDeletechannelTool
    tools.append(MicrosoftteamsDeletechannelTool())
    from .get import MicrosoftteamsGetTool
    tools.append(MicrosoftteamsGetTool())
    from .getall import MicrosoftteamsGetallTool
    tools.append(MicrosoftteamsGetallTool())
    from .update import MicrosoftteamsUpdateTool
    tools.append(MicrosoftteamsUpdateTool())
    from .create import MicrosoftteamsCreateTool
    tools.append(MicrosoftteamsCreateTool())
    from .getall import MicrosoftteamsGetallTool
    tools.append(MicrosoftteamsGetallTool())
    from .create import MicrosoftteamsCreateTool
    tools.append(MicrosoftteamsCreateTool())
    from .get import MicrosoftteamsGetTool
    tools.append(MicrosoftteamsGetTool())
    from .getall import MicrosoftteamsGetallTool
    tools.append(MicrosoftteamsGetallTool())
    from .create import MicrosoftteamsCreateTool
    tools.append(MicrosoftteamsCreateTool())
    from .deletetask import MicrosoftteamsDeletetaskTool
    tools.append(MicrosoftteamsDeletetaskTool())
    from .get import MicrosoftteamsGetTool
    tools.append(MicrosoftteamsGetTool())
    from .getall import MicrosoftteamsGetallTool
    tools.append(MicrosoftteamsGetallTool())
    from .update import MicrosoftteamsUpdateTool
    tools.append(MicrosoftteamsUpdateTool())
    return tools
