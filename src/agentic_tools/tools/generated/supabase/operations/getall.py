from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SupabaseCredentials

class SupabaseGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter to decide which rows get retrieved")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Filter")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class SupabaseGetallTool(BaseTool):
    name: str = "supabase_getall"
    connector_id: str = "nodes-base.supabase"
    description: str = "Tool for supabase getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = SupabaseGetallToolInput
    credentials: Optional[SupabaseCredentials] = None
