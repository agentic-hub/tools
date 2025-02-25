from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StrapiUpdateToolInput(BaseModel):
    updateKey: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entryId: Optional[str] = Field(None, description="The ID of the entry to delete")
    contentType: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiUpdateTool(BaseTool):
    name = "strapi_update"
    description = "Tool for strapi update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the strapi update operation."""
        # Implement the tool logic here
        return f"Running strapi update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strapi update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
