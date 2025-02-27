from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SupabaseCredentials

class SupabaseDeleteToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter to decide which rows get deleted")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Select Type")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class SupabaseDeleteTool(BaseTool):
    name: str = "supabase_delete"
    description: str = "Tool for supabase delete operation - delete operation"
    args_schema: type[BaseModel] | None = SupabaseDeleteToolInput
    credentials: Optional[SupabaseCredentials] = None
