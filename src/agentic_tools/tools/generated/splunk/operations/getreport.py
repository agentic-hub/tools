from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SplunkCredentials

class SplunkGetreportToolInput(BaseModel):
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


class SplunkGetreportTool(BaseTool):
    name: str = "splunk_getreport"
    connector_id: str = "nodes-base.splunk"
    description: str = "Tool for splunk getReport operation - getReport operation"
    args_schema: type[BaseModel] | None = SplunkGetreportToolInput
    credentials: Optional[SplunkCredentials] = None
