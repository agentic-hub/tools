from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GsuiteadminCredentials

class Gsuiteadmin__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="The value can be the user's primary email address, alias email address, or unique user ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    group_id: Optional[str] = Field(None, description="Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.")
    projection: Optional[str] = Field(None, description="What subset of fields to fetch for this user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class Gsuiteadmin__custom_api_call__Tool(BaseTool):
    name: str = "gsuiteadmin___custom_api_call__"
    description: str = "Tool for gSuiteAdmin __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Gsuiteadmin__custom_api_call__ToolInput
    credentials: Optional[GsuiteadminCredentials] = None
