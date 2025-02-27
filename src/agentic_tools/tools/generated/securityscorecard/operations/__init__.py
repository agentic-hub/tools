# securityScorecard operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import SecurityscorecardCredentials

def get_tools() -> List[BaseTool]:
    """Get all securityScorecard operation tools."""
    tools = []
    from .getfactor import SecurityscorecardGetfactorTool
    tools.append(SecurityscorecardGetfactorTool())
    from .getfactorhistorical import SecurityscorecardGetfactorhistoricalTool
    tools.append(SecurityscorecardGetfactorhistoricalTool())
    from .gethistoricalscore import SecurityscorecardGethistoricalscoreTool
    tools.append(SecurityscorecardGethistoricalscoreTool())
    from .getscorecard import SecurityscorecardGetscorecardTool
    tools.append(SecurityscorecardGetscorecardTool())
    from .getscoreplan import SecurityscorecardGetscoreplanTool
    tools.append(SecurityscorecardGetscoreplanTool())
    from .getfactor import SecurityscorecardGetfactorTool
    tools.append(SecurityscorecardGetfactorTool())
    from .getfactorhistorical import SecurityscorecardGetfactorhistoricalTool
    tools.append(SecurityscorecardGetfactorhistoricalTool())
    from .getscore import SecurityscorecardGetscoreTool
    tools.append(SecurityscorecardGetscoreTool())
    from .create import SecurityscorecardCreateTool
    tools.append(SecurityscorecardCreateTool())
    from .create import SecurityscorecardCreateTool
    tools.append(SecurityscorecardCreateTool())
    from .delete import SecurityscorecardDeleteTool
    tools.append(SecurityscorecardDeleteTool())
    from .getall import SecurityscorecardGetallTool
    tools.append(SecurityscorecardGetallTool())
    from .update import SecurityscorecardUpdateTool
    tools.append(SecurityscorecardUpdateTool())
    from .add import SecurityscorecardAddTool
    tools.append(SecurityscorecardAddTool())
    from .getall import SecurityscorecardGetallTool
    tools.append(SecurityscorecardGetallTool())
    from .remove import SecurityscorecardRemoveTool
    tools.append(SecurityscorecardRemoveTool())
    from .download import SecurityscorecardDownloadTool
    tools.append(SecurityscorecardDownloadTool())
    from .generate import SecurityscorecardGenerateTool
    tools.append(SecurityscorecardGenerateTool())
    from .getall import SecurityscorecardGetallTool
    tools.append(SecurityscorecardGetallTool())
    return tools
