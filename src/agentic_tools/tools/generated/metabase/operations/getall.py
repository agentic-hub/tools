from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MetabaseGetallToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseGetallTool(BaseTool):
    name = "metabase_getall"
    description = "Tool for metabase getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the metabase getAll operation."""
        # Implement the tool logic here
        return f"Running metabase getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the metabase getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
