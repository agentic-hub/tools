from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ProfitwellGetsettingToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ProfitwellGetsettingTool(BaseTool):
    name = "profitwell_getsetting"
    description = "Tool for profitWell getSetting operation - getSetting operation"
    
    def _run(self, **kwargs):
        """Run the profitWell getSetting operation."""
        # Implement the tool logic here
        return f"Running profitWell getSetting operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the profitWell getSetting operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
