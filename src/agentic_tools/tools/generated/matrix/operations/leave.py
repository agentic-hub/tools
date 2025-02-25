from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixLeaveToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    userId: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixLeaveTool(BaseTool):
    name = "matrix_leave"
    description = "Tool for matrix leave operation - leave operation"
    
    def _run(self, **kwargs):
        """Run the matrix leave operation."""
        # Implement the tool logic here
        return f"Running matrix leave operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix leave operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
