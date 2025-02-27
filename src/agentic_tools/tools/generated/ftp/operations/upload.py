from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FtpCredentials

class FtpUploadToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    file_content: Optional[str] = Field(None, description="The text content of the file to upload")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to upload. Has to contain the full path.")
    binary_data: Optional[bool] = Field(None, description="The text content of the file to upload")


class FtpUploadTool(BaseTool):
    name: str = "ftp_upload"
    connector_id: str = "nodes-base.ftp"
    description: str = "Tool for ftp upload operation - upload operation"
    args_schema: type[BaseModel] | None = FtpUploadToolInput
    credentials: Optional[FtpCredentials] = None
