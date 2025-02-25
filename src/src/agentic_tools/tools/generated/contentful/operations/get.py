from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ContentfulGetToolInput(BaseModel):
    source: Optional[str] = Field(None, description="Pick where your data comes from, delivery or preview API")
    contentTypeId: Optional[str] = Field(None, description="Content Type ID")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    entryId: Optional[str] = Field(None, description="Entry ID")
    assetId: Optional[str] = Field(None, description="Asset ID")
    environmentId: Optional[str] = Field(None, description="The ID for the Contentful environment (e.g. master, staging, etc.). Depending on your plan, you might not have environments. In that case use \"master\".")
    operation: Optional[str] = Field(None, description="Operation")


class ContentfulGetTool(BaseTool):
    name = "contentful_get"
    description = "Tool for contentful get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the contentful get operation."""
        # Implement the tool logic here
        return f"Running contentful get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the contentful get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
