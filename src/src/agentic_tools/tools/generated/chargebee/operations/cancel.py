from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeCancelToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    endOfTerm: Optional[bool] = Field(None, description="Whether it will not cancel it directly in will instead schedule the cancelation for the end of the term")
    operation: Optional[str] = Field(None, description="Operation")
    subscriptionId: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeCancelTool(BaseTool):
    name = "chargebee_cancel"
    description = "Tool for chargebee cancel operation - cancel operation"
    
    def _run(self, **kwargs):
        """Run the chargebee cancel operation."""
        # Implement the tool logic here
        return f"Running chargebee cancel operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee cancel operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
