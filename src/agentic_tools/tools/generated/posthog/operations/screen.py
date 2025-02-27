from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PosthogCredentials

class PosthogScreenToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    distinct_id: Optional[str] = Field(None, description="The user's distinct ID")
    operation: Optional[str] = Field(None, description="Operation")


class PosthogScreenTool(BaseTool):
    name: str = "posthog_screen"
    connector_id: str = "nodes-base.postHog"
    description: str = "Tool for postHog screen operation - screen operation"
    args_schema: type[BaseModel] | None = PosthogScreenToolInput
    credentials: Optional[PosthogCredentials] = None
