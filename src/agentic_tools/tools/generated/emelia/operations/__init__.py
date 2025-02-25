# emelia operations
from typing import List
from langchain.tools import BaseTool
from .. import EmeliaCredentials

def get_tools() -> List[BaseTool]:
    """Get all emelia operation tools."""
    tools = []
    from .addcontact import EmeliaAddcontactTool
    tools.append(EmeliaAddcontactTool())
    from .create import EmeliaCreateTool
    tools.append(EmeliaCreateTool())
    from .duplicate import EmeliaDuplicateTool
    tools.append(EmeliaDuplicateTool())
    from .get import EmeliaGetTool
    tools.append(EmeliaGetTool())
    from .getall import EmeliaGetallTool
    tools.append(EmeliaGetallTool())
    from .pause import EmeliaPauseTool
    tools.append(EmeliaPauseTool())
    from .start import EmeliaStartTool
    tools.append(EmeliaStartTool())
    from .add import EmeliaAddTool
    tools.append(EmeliaAddTool())
    from .getall import EmeliaGetallTool
    tools.append(EmeliaGetallTool())
    return tools
