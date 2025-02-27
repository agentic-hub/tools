from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NextcloudCredentials

class NextcloudDeleteToolInput(BaseModel):
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The path to delete. Can be a single file or a whole folder. The path should start with \"/\".")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudDeleteTool(BaseTool):
    name: str = "nextcloud_delete"
    description: str = "Tool for nextCloud delete operation - delete operation"
    args_schema: type[BaseModel] | None = NextcloudDeleteToolInput
    credentials: Optional[NextcloudCredentials] = None
