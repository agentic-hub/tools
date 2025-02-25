from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StrapiGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    entryId: Optional[str] = Field(None, description="The ID of the entry to delete")
    contentType: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiGetallTool(BaseTool):
    name = "strapi_getall"
    description = "Tool for strapi getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the strapi getAll operation."""
        # Implement the tool logic here
        return f"Running strapi getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strapi getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
