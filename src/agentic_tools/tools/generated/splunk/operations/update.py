from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SplunkCredentials

class SplunkUpdateToolInput(BaseModel):
    search_configuration_id: Optional[str] = Field(None, description="ID of the search configuration to delete")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="ID of the user to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    search_job_id: Optional[str] = Field(None, description="ID of the search job to delete")
    roles: Optional[str] = Field(None, description="roles")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkUpdateTool(BaseTool):
    name: str = "splunk_update"
    connector_id: str = "nodes-base.splunk"
    description: str = "Tool for splunk update operation - update operation"
    args_schema: type[BaseModel] | None = SplunkUpdateToolInput
    credentials: Optional[SplunkCredentials] = None
