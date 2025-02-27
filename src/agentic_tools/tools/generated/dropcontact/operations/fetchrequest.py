from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DropcontactCredentials

class DropcontactFetchrequestToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    request_id: Optional[str] = Field(None, description="Request ID")
    operation: Optional[str] = Field(None, description="Operation")


class DropcontactFetchrequestTool(BaseTool):
    name: str = "dropcontact_fetchrequest"
    connector_id: str = "nodes-base.dropcontact"
    description: str = "Tool for dropcontact fetchRequest operation - fetchRequest operation"
    args_schema: type[BaseModel] | None = DropcontactFetchrequestToolInput
    credentials: Optional[DropcontactCredentials] = None
