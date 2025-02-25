from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BubbleUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    objectId: Optional[str] = Field(None, description="ID of the object to update")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    typeName: Optional[str] = Field(None, description="Name of data type of the object to update")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleUpdateTool(BaseTool):
    name = "bubble_update"
    description = "Tool for bubble update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the bubble update operation."""
        # Implement the tool logic here
        return f"Running bubble update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bubble update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
