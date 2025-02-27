from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class NpmGetversionsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmGetversionsTool(BaseTool):
    name: str = "npm_getversions"
    description: str = "Tool for npm getVersions operation - getVersions operation"
    args_schema: type[BaseModel] | None = NpmGetversionsToolInput
    credentials: Optional[NpmCredentials] = None
