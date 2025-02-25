from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ProfitwellGetToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    month: Optional[str] = Field(None, description="Can only be the current or previous month. Format should be YYYY-MM.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class ProfitwellGetTool(BaseTool):
    name = "profitwell_get"
    description = "Tool for profitWell get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the profitWell get operation."""
        # Implement the tool logic here
        return f"Running profitWell get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the profitWell get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
