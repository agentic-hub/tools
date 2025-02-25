# googleFirebaseRealtimeDatabase toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlefirebaserealtimedatabase_tools() -> List[BaseTool]:
    """Get all googleFirebaseRealtimeDatabase tools."""
    from . import operations
    return operations.get_tools()
