from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhantombusterGetToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agentId: Optional[str] = Field(None, description="Agent ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetTool(BaseTool):
    name = "phantombuster_get"
    description = "Tool for phantombuster get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the phantombuster get operation."""
        # Implement the tool logic here
        return f"Running phantombuster get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the phantombuster get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
