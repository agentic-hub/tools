from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FtpCredentials

class FtpRenameToolInput(BaseModel):
    old_path: Optional[str] = Field(None, description="Old Path")
    new_path: Optional[str] = Field(None, description="New Path")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to delete. Has to contain the full path.")


class FtpRenameTool(BaseTool):
    name: str = "ftp_rename"
    description: str = "Tool for ftp rename operation - rename operation"
    args_schema: type[BaseModel] | None = FtpRenameToolInput
    credentials: Optional[FtpCredentials] = None
