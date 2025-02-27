from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SplunkCredentials

class SplunkCreateToolInput(BaseModel):
    search_configuration_id: Optional[str] = Field(None, description="ID of the search configuration to delete")
    name: Optional[str] = Field(None, description="Login name of the user")
    search: Optional[str] = Field(None, description="Search language string to execute, in Splunk's <a href=\"https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual\">Search Processing Language</a>")
    user_id: Optional[str] = Field(None, description="ID of the user to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    search_job_id: Optional[str] = Field(None, description="ID of the search job to delete")
    roles: Optional[str] = Field(None, description="roles")
    password: Optional[str] = Field(None, description="Password")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkCreateTool(BaseTool):
    name: str = "splunk_create"
    description: str = "Tool for splunk create operation - create operation"
    args_schema: type[BaseModel] | None = SplunkCreateToolInput
    credentials: Optional[SplunkCredentials] = None
