from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class NpmSearchToolInput(BaseModel):
    offset: Optional[float] = Field(None, description="Offset to return results from")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    package_name: Optional[str] = Field(None, description="Package Name")
    query: Optional[str] = Field(None, description="The query text used to search for packages")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmSearchTool(BaseTool):
    name: str = "npm_search"
    description: str = "Tool for npm search operation - search operation"
    args_schema: type[BaseModel] | None = NpmSearchToolInput
    credentials: Optional[NpmCredentials] = None
