# metabase operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MetabaseCredentials

def get_tools() -> List[BaseTool]:
    """Get all metabase operation tools."""
    tools = []
    from .get import MetabaseGetTool
    tools.append(MetabaseGetTool())
    from .getall import MetabaseGetallTool
    tools.append(MetabaseGetallTool())
    from .resultdata import MetabaseResultdataTool
    tools.append(MetabaseResultdataTool())
    from .__custom_api_call__ import Metabase__custom_api_call__Tool
    tools.append(Metabase__custom_api_call__Tool())
    from .get import MetabaseGetTool
    tools.append(MetabaseGetTool())
    from .getall import MetabaseGetallTool
    tools.append(MetabaseGetallTool())
    from .__custom_api_call__ import Metabase__custom_api_call__Tool
    tools.append(Metabase__custom_api_call__Tool())
    from .addnewdatasource import MetabaseAddnewdatasourceTool
    tools.append(MetabaseAddnewdatasourceTool())
    from .getall import MetabaseGetallTool
    tools.append(MetabaseGetallTool())
    from .getfields import MetabaseGetfieldsTool
    tools.append(MetabaseGetfieldsTool())
    from .__custom_api_call__ import Metabase__custom_api_call__Tool
    tools.append(Metabase__custom_api_call__Tool())
    from .get import MetabaseGetTool
    tools.append(MetabaseGetTool())
    from .getall import MetabaseGetallTool
    tools.append(MetabaseGetallTool())
    from .__custom_api_call__ import Metabase__custom_api_call__Tool
    tools.append(Metabase__custom_api_call__Tool())
    return tools
