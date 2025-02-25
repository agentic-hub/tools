from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MatrixJoinToolInput(BaseModel):
    roomId: Optional[str] = Field(None, description="The room related to the event")
    userId: Optional[str] = Field(None, description="The fully qualified user ID of the invitee")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")
    roomIdOrAlias: Optional[str] = Field(None, description="Room ID or Alias")


class MatrixJoinTool(BaseTool):
    name = "matrix_join"
    description = "Tool for matrix join operation - join operation"
    
    def _run(self, **kwargs):
        """Run the matrix join operation."""
        # Implement the tool logic here
        return f"Running matrix join operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the matrix join operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
