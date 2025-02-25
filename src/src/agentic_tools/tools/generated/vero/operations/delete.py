from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VeroDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    dataAttributesJson: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    dataAttributesUi: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the user")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class VeroDeleteTool(BaseTool):
    name = "vero_delete"
    description = "Tool for vero delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the vero delete operation."""
        # Implement the tool logic here
        return f"Running vero delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the vero delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
