from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FtpCredentials

class FtpListToolInput(BaseModel):
    recursive: Optional[bool] = Field(None, description="Whether to return object representing all directories / objects recursively found within SFTP server")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Path of directory to list contents of")


class FtpListTool(BaseTool):
    name: str = "ftp_list"
    description: str = "Tool for ftp list operation - list operation"
    args_schema: type[BaseModel] | None = FtpListToolInput
    credentials: Optional[FtpCredentials] = None
