from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeListToolInput(BaseModel):
    maxResults: Optional[float] = Field(None, description="Max. amount of results to return(< 100).")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter for invoices")
    subscriptionId: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeListTool(BaseTool):
    name = "chargebee_list"
    description = "Tool for chargebee list operation - list operation"
    
    def _run(self, **kwargs):
        """Run the chargebee list operation."""
        # Implement the tool logic here
        return f"Running chargebee list operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee list operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
