from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PosthogCredentials

class PosthogCreateToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="The name of the event")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    alias: Optional[str] = Field(None, description="The name of the alias")
    distinct_id: Optional[str] = Field(None, description="The user's distinct ID")
    operation: Optional[str] = Field(None, description="Operation")


class PosthogCreateTool(BaseTool):
    name: str = "posthog_create"
    connector_id: str = "nodes-base.postHog"
    description: str = "Tool for postHog create operation - create operation"
    args_schema: type[BaseModel] | None = PosthogCreateToolInput
    credentials: Optional[PosthogCredentials] = None
