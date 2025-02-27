from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PosthogCredentials

class PosthogPageToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    distinct_id: Optional[str] = Field(None, description="The user's distinct ID")
    operation: Optional[str] = Field(None, description="Operation")


class PosthogPageTool(BaseTool):
    name: str = "posthog_page"
    connector_id: str = "nodes-base.postHog"
    description: str = "Tool for postHog page operation - page operation"
    args_schema: type[BaseModel] | None = PosthogPageToolInput
    credentials: Optional[PosthogCredentials] = None
