from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpListToolInput(BaseModel):
    recursive: Optional[bool] = Field(None, description="Whether to return object representing all directories / objects recursively found within SFTP server")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Path of directory to list contents of")


class FtpListTool(BaseTool):
    name = "ftp_list"
    description = "Tool for ftp list operation - list operation"
    
    def _run(self, **kwargs):
        """Run the ftp list operation."""
        # Implement the tool logic here
        return f"Running ftp list operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp list operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
