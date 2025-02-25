from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpDeleteToolInput(BaseModel):
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to delete. Has to contain the full path.")


class FtpDeleteTool(BaseTool):
    name = "ftp_delete"
    description = "Tool for ftp delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the ftp delete operation."""
        # Implement the tool logic here
        return f"Running ftp delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
