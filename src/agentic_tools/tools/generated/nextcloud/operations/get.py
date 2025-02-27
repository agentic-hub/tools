from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NextcloudCredentials

class NextcloudGetToolInput(BaseModel):
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The path of file or folder to copy. The path should start with \"/\".")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudGetTool(BaseTool):
    name: str = "nextcloud_get"
    description: str = "Tool for nextCloud get operation - get operation"
    args_schema: type[BaseModel] | None = NextcloudGetToolInput
    credentials: Optional[NextcloudCredentials] = None
