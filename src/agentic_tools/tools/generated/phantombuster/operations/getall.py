from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PhantombusterGetallToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agentId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetallTool(BaseTool):
    name = "phantombuster_getall"
    description = "Tool for phantombuster getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the phantombuster getAll operation."""
        # Implement the tool logic here
        return f"Running phantombuster getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the phantombuster getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
