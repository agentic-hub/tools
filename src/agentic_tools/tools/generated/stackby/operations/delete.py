from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StackbyDeleteToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Enter Table Name")
    id: Optional[str] = Field(None, description="ID of the record to return")
    operation: Optional[str] = Field(None, description="Operation")
    stackId: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyDeleteTool(BaseTool):
    name = "stackby_delete"
    description = "Tool for stackby delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the stackby delete operation."""
        # Implement the tool logic here
        return f"Running stackby delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stackby delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
