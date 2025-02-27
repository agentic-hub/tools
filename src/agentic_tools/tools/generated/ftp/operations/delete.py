from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FtpCredentials

class FtpDeleteToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to delete. Has to contain the full path.")


class FtpDeleteTool(BaseTool):
    name: str = "ftp_delete"
    connector_id: str = "nodes-base.ftp"
    description: str = "Tool for ftp delete operation - delete operation"
    args_schema: type[BaseModel] | None = FtpDeleteToolInput
    credentials: Optional[FtpCredentials] = None
