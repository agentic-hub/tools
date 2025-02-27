from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantGeterrologsToolInput(BaseModel):
    entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class HomeassistantGeterrologsTool(BaseTool):
    name: str = "homeassistant_geterrologs"
    connector_id: str = "nodes-base.homeAssistant"
    description: str = "Tool for homeAssistant getErroLogs operation - getErroLogs operation"
    args_schema: type[BaseModel] | None = HomeassistantGeterrologsToolInput
    credentials: Optional[HomeassistantCredentials] = None
