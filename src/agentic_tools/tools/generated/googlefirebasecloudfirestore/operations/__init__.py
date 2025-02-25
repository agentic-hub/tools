# googleFirebaseCloudFirestore operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all googleFirebaseCloudFirestore operation tools."""
    tools = []
    from .create import GooglefirebasecloudfirestoreCreateTool
    tools.append(GooglefirebasecloudfirestoreCreateTool())
    from .upsert import GooglefirebasecloudfirestoreUpsertTool
    tools.append(GooglefirebasecloudfirestoreUpsertTool())
    from .delete import GooglefirebasecloudfirestoreDeleteTool
    tools.append(GooglefirebasecloudfirestoreDeleteTool())
    from .get import GooglefirebasecloudfirestoreGetTool
    tools.append(GooglefirebasecloudfirestoreGetTool())
    from .getall import GooglefirebasecloudfirestoreGetallTool
    tools.append(GooglefirebasecloudfirestoreGetallTool())
    from .query import GooglefirebasecloudfirestoreQueryTool
    tools.append(GooglefirebasecloudfirestoreQueryTool())
    from .__custom_api_call__ import Googlefirebasecloudfirestore__custom_api_call__Tool
    tools.append(Googlefirebasecloudfirestore__custom_api_call__Tool())
    from .getall import GooglefirebasecloudfirestoreGetallTool
    tools.append(GooglefirebasecloudfirestoreGetallTool())
    from .__custom_api_call__ import Googlefirebasecloudfirestore__custom_api_call__Tool
    tools.append(Googlefirebasecloudfirestore__custom_api_call__Tool())
    return tools
