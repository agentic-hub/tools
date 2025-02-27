from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NextcloudCredentials

class NextcloudShareToolInput(BaseModel):
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The file path of the file to share. Has to contain the full path. The path should start with \"/\".")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    share_type: Optional[str] = Field(None, description="The share permissions to set")
    circle_id: Optional[str] = Field(None, description="The ID of the circle to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    group_id: Optional[str] = Field(None, description="The ID of the group to share with")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[str] = Field(None, description="The user to share with")


class NextcloudShareTool(BaseTool):
    name: str = "nextcloud_share"
    description: str = "Tool for nextCloud share operation - share operation"
    args_schema: type[BaseModel] | None = NextcloudShareToolInput
    credentials: Optional[NextcloudCredentials] = None
