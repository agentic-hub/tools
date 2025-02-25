from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OuraGetsleepToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class OuraGetsleepTool(BaseTool):
    name = "oura_getsleep"
    description = "Tool for oura getSleep operation - getSleep operation"
    
    def _run(self, **kwargs):
        """Run the oura getSleep operation."""
        # Implement the tool logic here
        return f"Running oura getSleep operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oura getSleep operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
