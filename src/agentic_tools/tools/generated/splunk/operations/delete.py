from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SplunkCredentials

class SplunkDeleteToolInput(BaseModel):
    search_configuration_id: Optional[str] = Field(None, description="ID of the search configuration to delete")
    user_id: Optional[str] = Field(None, description="ID of the user to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    search_job_id: Optional[str] = Field(None, description="ID of the search job to delete")
    roles: Optional[str] = Field(None, description="roles")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkDeleteTool(BaseTool):
    name: str = "splunk_delete"
    description: str = "Tool for splunk delete operation - delete operation"
    args_schema: type[BaseModel] | None = SplunkDeleteToolInput
    credentials: Optional[SplunkCredentials] = None
