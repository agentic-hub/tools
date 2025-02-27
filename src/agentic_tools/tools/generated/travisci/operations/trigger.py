from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TravisciCredentials

class TravisciTriggerToolInput(BaseModel):
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    slug: Optional[str] = Field(None, description="Same as {ownerName}/{repositoryName}")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    branch: Optional[str] = Field(None, description="Branch requested to be built")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciTriggerTool(BaseTool):
    name: str = "travisci_trigger"
    connector_id: str = "nodes-base.travisCi"
    description: str = "Tool for travisCi trigger operation - trigger operation"
    args_schema: type[BaseModel] | None = TravisciTriggerToolInput
    credentials: Optional[TravisciCredentials] = None
