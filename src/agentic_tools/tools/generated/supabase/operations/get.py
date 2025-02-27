from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SupabaseCredentials

class SupabaseGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Select Conditions")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Select Type")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class SupabaseGetTool(BaseTool):
    name: str = "supabase_get"
    connector_id: str = "nodes-base.supabase"
    description: str = "Tool for supabase get operation - get operation"
    args_schema: type[BaseModel] | None = SupabaseGetToolInput
    credentials: Optional[SupabaseCredentials] = None
