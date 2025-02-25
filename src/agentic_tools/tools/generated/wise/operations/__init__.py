# wise operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all wise operation tools."""
    tools = []
    from .getbalances import WiseGetbalancesTool
    tools.append(WiseGetbalancesTool())
    from .getcurrencies import WiseGetcurrenciesTool
    tools.append(WiseGetcurrenciesTool())
    from .getstatement import WiseGetstatementTool
    tools.append(WiseGetstatementTool())
    from .get import WiseGetTool
    tools.append(WiseGetTool())
    from .get import WiseGetTool
    tools.append(WiseGetTool())
    from .getall import WiseGetallTool
    tools.append(WiseGetallTool())
    from .create import WiseCreateTool
    tools.append(WiseCreateTool())
    from .get import WiseGetTool
    tools.append(WiseGetTool())
    from .getall import WiseGetallTool
    tools.append(WiseGetallTool())
    from .create import WiseCreateTool
    tools.append(WiseCreateTool())
    from .delete import WiseDeleteTool
    tools.append(WiseDeleteTool())
    from .execute import WiseExecuteTool
    tools.append(WiseExecuteTool())
    from .get import WiseGetTool
    tools.append(WiseGetTool())
    from .getall import WiseGetallTool
    tools.append(WiseGetallTool())
    return tools
