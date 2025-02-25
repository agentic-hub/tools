# supabase operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all supabase operation tools."""
    tools = []
    from .create import SupabaseCreateTool
    tools.append(SupabaseCreateTool())
    from .delete import SupabaseDeleteTool
    tools.append(SupabaseDeleteTool())
    from .get import SupabaseGetTool
    tools.append(SupabaseGetTool())
    from .getall import SupabaseGetallTool
    tools.append(SupabaseGetallTool())
    from .update import SupabaseUpdateTool
    tools.append(SupabaseUpdateTool())
    from .__custom_api_call__ import Supabase__custom_api_call__Tool
    tools.append(Supabase__custom_api_call__Tool())
    return tools
