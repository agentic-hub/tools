from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PagerdutyCredentials

class PagerdutyCreateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The note content")
    conference_bridge_ui: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    service_id: Optional[str] = Field(None, description="The incident will be created on this service. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    title: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the incident")
    operation: Optional[str] = Field(None, description="Operation")
    incident_id: Optional[str] = Field(None, description="Unique identifier for the incident")


class PagerdutyCreateTool(BaseTool):
    name: str = "pagerduty_create"
    description: str = "Tool for pagerDuty create operation - create operation"
    args_schema: type[BaseModel] | None = PagerdutyCreateToolInput
    credentials: Optional[PagerdutyCredentials] = None
