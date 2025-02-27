from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GotifyCredentials

class GotifyDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Message ID")


class GotifyDeleteTool(BaseTool):
    name: str = "gotify_delete"
    connector_id: str = "nodes-base.gotify"
    description: str = "Tool for gotify delete operation - delete operation"
    args_schema: type[BaseModel] | None = GotifyDeleteToolInput
    credentials: Optional[GotifyCredentials] = None
