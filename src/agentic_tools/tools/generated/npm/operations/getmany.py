from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class NpmGetmanyToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmGetmanyTool(BaseTool):
    name: str = "npm_getmany"
    connector_id: str = "nodes-base.npm"
    description: str = "Tool for npm getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = NpmGetmanyToolInput
    credentials: Optional[NpmCredentials] = None
