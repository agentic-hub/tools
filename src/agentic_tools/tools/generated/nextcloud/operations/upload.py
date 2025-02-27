from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NextcloudCredentials

class NextcloudUploadToolInput(BaseModel):
    to_path: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The absolute file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten.")
    user_id: Optional[str] = Field(None, description="Username the user will have")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    file_content: Optional[str] = Field(None, description="The text content of the file to upload")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    binary_data_upload: Optional[bool] = Field(None, description="Binary File")


class NextcloudUploadTool(BaseTool):
    name: str = "nextcloud_upload"
    connector_id: str = "nodes-base.nextCloud"
    description: str = "Tool for nextCloud upload operation - upload operation"
    args_schema: type[BaseModel] | None = NextcloudUploadToolInput
    credentials: Optional[NextcloudCredentials] = None
