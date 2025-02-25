from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixGetToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="The room related to the event")
    userId: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    eventId: Optional[str] = Field(None, description="The room related to the event")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixGetTool(BaseTool):
    name = "matrix_get"
    description = "Tool for matrix get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the matrix get operation."""
        # Implement the tool logic here
        return f"Running matrix get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
