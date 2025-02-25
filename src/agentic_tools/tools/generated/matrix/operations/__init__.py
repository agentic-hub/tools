# matrix operations
from typing import List
from langchain.tools import BaseTool
from .. import MatrixCredentials

def get_tools() -> List[BaseTool]:
    """Get all matrix operation tools."""
    tools = []
    from .me import MatrixMeTool
    tools.append(MatrixMeTool())
    from .get import MatrixGetTool
    tools.append(MatrixGetTool())
    from .upload import MatrixUploadTool
    tools.append(MatrixUploadTool())
    from .create import MatrixCreateTool
    tools.append(MatrixCreateTool())
    from .getall import MatrixGetallTool
    tools.append(MatrixGetallTool())
    from .create import MatrixCreateTool
    tools.append(MatrixCreateTool())
    from .invite import MatrixInviteTool
    tools.append(MatrixInviteTool())
    from .join import MatrixJoinTool
    tools.append(MatrixJoinTool())
    from .kick import MatrixKickTool
    tools.append(MatrixKickTool())
    from .leave import MatrixLeaveTool
    tools.append(MatrixLeaveTool())
    from .getall import MatrixGetallTool
    tools.append(MatrixGetallTool())
    return tools
