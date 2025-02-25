from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixKickToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reason: Optional[str] = Field(None, description="Reason for kick")
    userId: Optional[str] = Field(None, description="The fully qualified user ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixKickTool(BaseTool):
    name = "matrix_kick"
    description = "Tool for matrix kick operation - kick operation"
    
    def _run(self, **kwargs):
        """Run the matrix kick operation."""
        # Implement the tool logic here
        return f"Running matrix kick operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix kick operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
