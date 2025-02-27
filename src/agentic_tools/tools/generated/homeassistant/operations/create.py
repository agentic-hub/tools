from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantCreateToolInput(BaseModel):
    entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    template: Optional[str] = Field(None, description="Render a Home Assistant template. <a href=\"https://www.home-assistant.io/docs/configuration/templating/\">See template docs for more information.</a>.")
    event_attributes: Optional[Dict[str, Any]] = Field(None, description="Event Attributes")
    operation: Optional[str] = Field(None, description="Operation")
    event_type: Optional[str] = Field(None, description="The Entity ID for which an event will be created")


class HomeassistantCreateTool(BaseTool):
    name: str = "homeassistant_create"
    connector_id: str = "nodes-base.homeAssistant"
    description: str = "Tool for homeAssistant create operation - create operation"
    args_schema: type[BaseModel] | None = HomeassistantCreateToolInput
    credentials: Optional[HomeassistantCredentials] = None
