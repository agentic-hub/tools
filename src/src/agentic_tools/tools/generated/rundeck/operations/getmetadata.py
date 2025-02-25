from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RundeckGetmetadataToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    jobid: Optional[str] = Field(None, description="The job ID to get metadata off")
    operation: Optional[str] = Field(None, description="Operation")


class RundeckGetmetadataTool(BaseTool):
    name = "rundeck_getmetadata"
    description = "Tool for rundeck getMetadata operation - getMetadata operation"
    
    def _run(self, **kwargs):
        """Run the rundeck getMetadata operation."""
        # Implement the tool logic here
        return f"Running rundeck getMetadata operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rundeck getMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
