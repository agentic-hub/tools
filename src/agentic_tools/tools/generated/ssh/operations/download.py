from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SshCredentials

class SshDownloadToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Object property name which holds binary data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path including file name.")


class SshDownloadTool(BaseTool):
    name: str = "ssh_download"
    description: str = "Tool for ssh download operation - download operation"
    args_schema: type[BaseModel] | None = SshDownloadToolInput
    credentials: Optional[SshCredentials] = None
