from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NpmCredentials

class Npm__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class Npm__custom_api_call__Tool(BaseTool):
    name: str = "npm___custom_api_call__"
    description: str = "Tool for npm __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Npm__custom_api_call__ToolInput
    credentials: Optional[NpmCredentials] = None
