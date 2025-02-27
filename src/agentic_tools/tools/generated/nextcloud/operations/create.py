from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NextcloudCredentials

class NextcloudCreateToolInput(BaseModel):
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The folder to create. The parent folder has to exist. The path should start with \"/\".")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The email of the user to invite")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudCreateTool(BaseTool):
    name: str = "nextcloud_create"
    description: str = "Tool for nextCloud create operation - create operation"
    args_schema: type[BaseModel] | None = NextcloudCreateToolInput
    credentials: Optional[NextcloudCredentials] = None
