# convertKit operations
from typing import List
from langchain.tools import BaseTool
from .. import ConvertkitCredentials

def get_tools() -> List[BaseTool]:
    """Get all convertKit operation tools."""
    tools = []
    from .create import ConvertkitCreateTool
    tools.append(ConvertkitCreateTool())
    from .delete import ConvertkitDeleteTool
    tools.append(ConvertkitDeleteTool())
    from .getall import ConvertkitGetallTool
    tools.append(ConvertkitGetallTool())
    from .update import ConvertkitUpdateTool
    tools.append(ConvertkitUpdateTool())
    from .addsubscriber import ConvertkitAddsubscriberTool
    tools.append(ConvertkitAddsubscriberTool())
    from .getall import ConvertkitGetallTool
    tools.append(ConvertkitGetallTool())
    from .getsubscriptions import ConvertkitGetsubscriptionsTool
    tools.append(ConvertkitGetsubscriptionsTool())
    from .addsubscriber import ConvertkitAddsubscriberTool
    tools.append(ConvertkitAddsubscriberTool())
    from .getall import ConvertkitGetallTool
    tools.append(ConvertkitGetallTool())
    from .getsubscriptions import ConvertkitGetsubscriptionsTool
    tools.append(ConvertkitGetsubscriptionsTool())
    from .create import ConvertkitCreateTool
    tools.append(ConvertkitCreateTool())
    from .getall import ConvertkitGetallTool
    tools.append(ConvertkitGetallTool())
    from .add import ConvertkitAddTool
    tools.append(ConvertkitAddTool())
    from .getall import ConvertkitGetallTool
    tools.append(ConvertkitGetallTool())
    from .delete import ConvertkitDeleteTool
    tools.append(ConvertkitDeleteTool())
    return tools
