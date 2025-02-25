from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GetresponseGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    contactId: Optional[str] = Field(None, description="ID of contact to delete")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseGetallTool(BaseTool):
    name = "getresponse_getall"
    description = "Tool for getResponse getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the getResponse getAll operation."""
        # Implement the tool logic here
        return f"Running getResponse getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the getResponse getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
