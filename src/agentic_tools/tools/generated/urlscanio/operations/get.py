from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UrlscanioGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    scanId: Optional[str] = Field(None, description="ID of the scan to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioGetTool(BaseTool):
    name = "urlscanio_get"
    description = "Tool for urlScanIo get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the urlScanIo get operation."""
        # Implement the tool logic here
        return f"Running urlScanIo get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the urlScanIo get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
