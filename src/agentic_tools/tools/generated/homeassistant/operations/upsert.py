from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HomeassistantCredentials

class HomeassistantUpsertToolInput(BaseModel):
    entity_id: Optional[str] = Field(None, description="The entity ID for which a state will be created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    state: Optional[str] = Field(None, description="State")
    state_attributes: Optional[Dict[str, Any]] = Field(None, description="State Attributes")
    operation: Optional[str] = Field(None, description="Operation")


class HomeassistantUpsertTool(BaseTool):
    name: str = "homeassistant_upsert"
    description: str = "Tool for homeAssistant upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = HomeassistantUpsertToolInput
    credentials: Optional[HomeassistantCredentials] = None
