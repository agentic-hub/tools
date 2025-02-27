from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantGetToolInput(BaseModel):
    entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class HomeassistantGetTool(BaseTool):
    name: str = "homeassistant_get"
    connector_id: str = "nodes-base.homeAssistant"
    description: str = "Tool for homeAssistant get operation - get operation"
    args_schema: type[BaseModel] | None = HomeassistantGetToolInput
    credentials: Optional[HomeassistantCredentials] = None
