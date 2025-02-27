from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SupabaseCredentials

class SupabaseCreateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter to decide which rows get updated")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filter_type: Optional[str] = Field(None, description="Select Type")
    data_to_send: Optional[str] = Field(None, description="Data to Send")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    filter_string: Optional[str] = Field(None, description="Filters (String)")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://postgrest.org/en/v9.0/api.html#horizontal-filtering-rows\" target=\"_blank\">PostgREST guide</a> to creating filters")
    match_type: Optional[str] = Field(None, description="Must Match")


class SupabaseCreateTool(BaseTool):
    name: str = "supabase_create"
    connector_id: str = "nodes-base.supabase"
    description: str = "Tool for supabase create operation - create operation"
    args_schema: type[BaseModel] | None = SupabaseCreateToolInput
    credentials: Optional[SupabaseCredentials] = None
