from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BubbleCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    objectId: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    typeName: Optional[str] = Field(None, description="Name of data type of the object to create")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleCreateTool(BaseTool):
    name = "bubble_create"
    description = "Tool for bubble create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the bubble create operation."""
        # Implement the tool logic here
        return f"Running bubble create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bubble create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
