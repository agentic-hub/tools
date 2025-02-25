from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NpmGetmetadataToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    packageName: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    packageVersion: Optional[str] = Field(None, description="Package Version")


class NpmGetmetadataTool(BaseTool):
    name = "npm_getmetadata"
    description = "Tool for npm getMetadata operation - getMetadata operation"
    
    def _run(self, **kwargs):
        """Run the npm getMetadata operation."""
        # Implement the tool logic here
        return f"Running npm getMetadata operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the npm getMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
