from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpRenameToolInput(BaseModel):
    oldPath: Optional[str] = Field(None, description="Old Path")
    newPath: Optional[str] = Field(None, description="New Path")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to delete. Has to contain the full path.")


class FtpRenameTool(BaseTool):
    name = "ftp_rename"
    description = "Tool for ftp rename operation - rename operation"
    
    def _run(self, **kwargs):
        """Run the ftp rename operation."""
        # Implement the tool logic here
        return f"Running ftp rename operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp rename operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
