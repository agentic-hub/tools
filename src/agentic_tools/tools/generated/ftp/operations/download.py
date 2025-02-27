from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FtpCredentials

class FtpDownloadToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path.")


class FtpDownloadTool(BaseTool):
    name: str = "ftp_download"
    description: str = "Tool for ftp download operation - download operation"
    args_schema: type[BaseModel] | None = FtpDownloadToolInput
    credentials: Optional[FtpCredentials] = None
