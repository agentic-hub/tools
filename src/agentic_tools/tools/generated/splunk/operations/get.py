from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SplunkCredentials

class SplunkGetToolInput(BaseModel):
    search_configuration_id: Optional[str] = Field(None, description="ID of the search configuration to retrieve")
    user_id: Optional[str] = Field(None, description="ID of the user to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    search_job_id: Optional[str] = Field(None, description="ID of the search job to retrieve")
    roles: Optional[str] = Field(None, description="roles")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkGetTool(BaseTool):
    name: str = "splunk_get"
    connector_id: str = "nodes-base.splunk"
    description: str = "Tool for splunk get operation - get operation"
    args_schema: type[BaseModel] | None = SplunkGetToolInput
    credentials: Optional[SplunkCredentials] = None
