from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixInviteToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    userId: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MatrixInviteTool(BaseTool):
    name = "matrix_invite"
    description = "Tool for matrix invite operation - invite operation"
    
    def _run(self, **kwargs):
        """Run the matrix invite operation."""
        # Implement the tool logic here
        return f"Running matrix invite operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix invite operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
