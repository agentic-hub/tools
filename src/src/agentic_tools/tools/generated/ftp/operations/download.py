from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpDownloadToolInput(BaseModel):
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path.")


class FtpDownloadTool(BaseTool):
    name = "ftp_download"
    description = "Tool for ftp download operation - download operation"
    
    def _run(self, **kwargs):
        """Run the ftp download operation."""
        # Implement the tool logic here
        return f"Running ftp download operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
