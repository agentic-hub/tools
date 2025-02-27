from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class NpmGetmetadataToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmGetmetadataTool(BaseTool):
    name: str = "npm_getmetadata"
    description: str = "Tool for npm getMetadata operation - getMetadata operation"
    args_schema: type[BaseModel] | None = NpmGetmetadataToolInput
    credentials: Optional[NpmCredentials] = None
