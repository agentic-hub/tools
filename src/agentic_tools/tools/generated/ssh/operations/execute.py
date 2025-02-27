from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SshCredentials

class SshExecuteToolInput(BaseModel):
    cwd: Optional[str] = Field(None, description="Working Directory")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    authentication: Optional[str] = Field(None, description="Authentication")
    command: Optional[str] = Field(None, description="The command to be executed on a remote device")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter \"File Name\" under options.")


class SshExecuteTool(BaseTool):
    name: str = "ssh_execute"
    description: str = "Tool for ssh execute operation - execute operation"
    args_schema: type[BaseModel] | None = SshExecuteToolInput
    credentials: Optional[SshCredentials] = None
