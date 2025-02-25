from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OuraGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class OuraGetTool(BaseTool):
    name = "oura_get"
    description = "Tool for oura get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the oura get operation."""
        # Implement the tool logic here
        return f"Running oura get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oura get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
