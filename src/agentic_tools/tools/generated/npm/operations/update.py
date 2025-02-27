from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class NpmUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    dist_tag_name: Optional[str] = Field(None, description="Distribution Tag Name")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmUpdateTool(BaseTool):
    name: str = "npm_update"
    description: str = "Tool for npm update operation - update operation"
    args_schema: type[BaseModel] | None = NpmUpdateToolInput
    credentials: Optional[NpmCredentials] = None
