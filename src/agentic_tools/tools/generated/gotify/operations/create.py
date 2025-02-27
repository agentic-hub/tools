from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GotifyCredentials

class GotifyCreateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send, If using Markdown add the Content Type option")
    operation: Optional[str] = Field(None, description="Operation")


class GotifyCreateTool(BaseTool):
    name: str = "gotify_create"
    connector_id: str = "nodes-base.gotify"
    description: str = "Tool for gotify create operation - create operation"
    args_schema: type[BaseModel] | None = GotifyCreateToolInput
    credentials: Optional[GotifyCredentials] = None
