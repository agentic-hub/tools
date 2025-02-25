from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    subscriptionId: Optional[str] = Field(None, description="The ID of the subscription to delete")


class ChargebeeDeleteTool(BaseTool):
    name = "chargebee_delete"
    description = "Tool for chargebee delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the chargebee delete operation."""
        # Implement the tool logic here
        return f"Running chargebee delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
