from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AdaloGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    collectionId: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    operation: Optional[str] = Field(None, description="Operation")


class AdaloGetallTool(BaseTool):
    name = "adalo_getall"
    description = "Tool for adalo getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the adalo getAll operation."""
        # Implement the tool logic here
        return f"Running adalo getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the adalo getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
