from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhantombusterDeleteToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agentId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterDeleteTool(BaseTool):
    name = "phantombuster_delete"
    description = "Tool for phantombuster delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the phantombuster delete operation."""
        # Implement the tool logic here
        return f"Running phantombuster delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the phantombuster delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
