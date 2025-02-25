from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NpmSearchToolInput(BaseModel):
    offset: Optional[float] = Field(None, description="Offset to return results from")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    packageName: Optional[str] = Field(None, description="Package Name")
    query: Optional[str] = Field(None, description="The query text used to search for packages")
    operation: Optional[str] = Field(None, description="Operation")
    packageVersion: Optional[str] = Field(None, description="Package Version")


class NpmSearchTool(BaseTool):
    name = "npm_search"
    description = "Tool for npm search operation - search operation"
    
    def _run(self, **kwargs):
        """Run the npm search operation."""
        # Implement the tool logic here
        return f"Running npm search operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the npm search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
