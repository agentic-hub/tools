from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SshCredentials

class SshUploadToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter \"File Name\" under options.")


class SshUploadTool(BaseTool):
    name: str = "ssh_upload"
    connector_id: str = "nodes-base.ssh"
    description: str = "Tool for ssh upload operation - upload operation"
    args_schema: type[BaseModel] | None = SshUploadToolInput
    credentials: Optional[SshCredentials] = None
