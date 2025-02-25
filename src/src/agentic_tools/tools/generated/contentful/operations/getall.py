from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ContentfulGetallToolInput(BaseModel):
    source: Optional[str] = Field(None, description="Pick where your data comes from, delivery or preview API")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    environmentId: Optional[str] = Field(None, description="The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".")
    operation: Optional[str] = Field(None, description="Operation")


class ContentfulGetallTool(BaseTool):
    name = "contentful_getall"
    description = "Tool for contentful getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the contentful getAll operation."""
        # Implement the tool logic here
        return f"Running contentful getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the contentful getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
