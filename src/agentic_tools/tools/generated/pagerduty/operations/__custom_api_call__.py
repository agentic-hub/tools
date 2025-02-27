from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PagerdutyCredentials

class Pagerduty__custom_api_call__ToolInput(BaseModel):
    conference_bridge_ui: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    incident_id: Optional[str] = Field(None, description="Unique identifier for the incident")


class Pagerduty__custom_api_call__Tool(BaseTool):
    name: str = "pagerduty___custom_api_call__"
    description: str = "Tool for pagerDuty __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Pagerduty__custom_api_call__ToolInput
    credentials: Optional[PagerdutyCredentials] = None
