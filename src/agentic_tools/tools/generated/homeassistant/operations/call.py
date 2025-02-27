from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantCallToolInput(BaseModel):
    domain: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    service: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    service_attributes: Optional[Dict[str, Any]] = Field(None, description="Service Attributes")
    operation: Optional[str] = Field(None, description="Operation")


class HomeassistantCallTool(BaseTool):
    name: str = "homeassistant_call"
    connector_id: str = "nodes-base.homeAssistant"
    description: str = "Tool for homeAssistant call operation - call operation"
    args_schema: type[BaseModel] | None = HomeassistantCallToolInput
    credentials: Optional[HomeassistantCredentials] = None
