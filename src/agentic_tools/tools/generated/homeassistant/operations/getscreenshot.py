from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantGetscreenshotToolInput(BaseModel):
    entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")
    camera_entity_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class HomeassistantGetscreenshotTool(BaseTool):
    name: str = "homeassistant_getscreenshot"
    connector_id: str = "nodes-base.homeAssistant"
    description: str = "Tool for homeAssistant getScreenshot operation - getScreenshot operation"
    args_schema: type[BaseModel] | None = HomeassistantGetscreenshotToolInput
    credentials: Optional[HomeassistantCredentials] = None
