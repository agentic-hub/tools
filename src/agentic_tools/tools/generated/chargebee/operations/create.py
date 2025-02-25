from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties to set on the new user")
    subscriptionId: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeCreateTool(BaseTool):
    name = "chargebee_create"
    description = "Tool for chargebee create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the chargebee create operation."""
        # Implement the tool logic here
        return f"Running chargebee create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
