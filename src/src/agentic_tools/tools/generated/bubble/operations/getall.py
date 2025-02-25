from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BubbleGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    objectId: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    typeName: Optional[str] = Field(None, description="Name of data type of the object to create")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleGetallTool(BaseTool):
    name = "bubble_getall"
    description = "Tool for bubble getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the bubble getAll operation."""
        # Implement the tool logic here
        return f"Running bubble getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bubble getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
