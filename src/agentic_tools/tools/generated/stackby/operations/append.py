from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StackbyAppendToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Enter Table Name")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")
    stackId: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyAppendTool(BaseTool):
    name = "stackby_append"
    description = "Tool for stackby append operation - append operation"
    
    def _run(self, **kwargs):
        """Run the stackby append operation."""
        # Implement the tool logic here
        return f"Running stackby append operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stackby append operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
