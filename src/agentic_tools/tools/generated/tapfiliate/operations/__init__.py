# tapfiliate operations
from typing import List
from langchain.tools import BaseTool
from .. import TapfiliateCredentials

def get_tools() -> List[BaseTool]:
    """Get all tapfiliate operation tools."""
    tools = []
    from .create import TapfiliateCreateTool
    tools.append(TapfiliateCreateTool())
    from .delete import TapfiliateDeleteTool
    tools.append(TapfiliateDeleteTool())
    from .get import TapfiliateGetTool
    tools.append(TapfiliateGetTool())
    from .getall import TapfiliateGetallTool
    tools.append(TapfiliateGetallTool())
    from .add import TapfiliateAddTool
    tools.append(TapfiliateAddTool())
    from .remove import TapfiliateRemoveTool
    tools.append(TapfiliateRemoveTool())
    from .update import TapfiliateUpdateTool
    tools.append(TapfiliateUpdateTool())
    from .add import TapfiliateAddTool
    tools.append(TapfiliateAddTool())
    from .approve import TapfiliateApproveTool
    tools.append(TapfiliateApproveTool())
    from .disapprove import TapfiliateDisapproveTool
    tools.append(TapfiliateDisapproveTool())
    from .get import TapfiliateGetTool
    tools.append(TapfiliateGetTool())
    from .getall import TapfiliateGetallTool
    tools.append(TapfiliateGetallTool())
    return tools
