# splunk operations
from typing import List
from langchain.tools import BaseTool
from .. import SplunkCredentials

def get_tools() -> List[BaseTool]:
    """Get all splunk operation tools."""
    tools = []
    from .getreport import SplunkGetreportTool
    tools.append(SplunkGetreportTool())
    from .delete import SplunkDeleteTool
    tools.append(SplunkDeleteTool())
    from .get import SplunkGetTool
    tools.append(SplunkGetTool())
    from .getall import SplunkGetallTool
    tools.append(SplunkGetallTool())
    from .create import SplunkCreateTool
    tools.append(SplunkCreateTool())
    from .delete import SplunkDeleteTool
    tools.append(SplunkDeleteTool())
    from .get import SplunkGetTool
    tools.append(SplunkGetTool())
    from .getall import SplunkGetallTool
    tools.append(SplunkGetallTool())
    from .getall import SplunkGetallTool
    tools.append(SplunkGetallTool())
    from .create import SplunkCreateTool
    tools.append(SplunkCreateTool())
    from .delete import SplunkDeleteTool
    tools.append(SplunkDeleteTool())
    from .get import SplunkGetTool
    tools.append(SplunkGetTool())
    from .getall import SplunkGetallTool
    tools.append(SplunkGetallTool())
    from .update import SplunkUpdateTool
    tools.append(SplunkUpdateTool())
    return tools
