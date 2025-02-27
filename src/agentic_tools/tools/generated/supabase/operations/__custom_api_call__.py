from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SupabaseCredentials

class Supabase__custom_api_call__ToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter to decide which rows get updated")
    resource: Optional[str] = Field(None, description="Resource")
    filter_type: Optional[str] = Field(None, description="Select Type")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class Supabase__custom_api_call__Tool(BaseTool):
    name: str = "supabase___custom_api_call__"
    description: str = "Tool for supabase __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Supabase__custom_api_call__ToolInput
    credentials: Optional[SupabaseCredentials] = None
