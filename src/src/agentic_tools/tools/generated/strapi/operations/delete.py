from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StrapiDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entryId: Optional[str] = Field(None, description="The ID of the entry to delete")
    contentType: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiDeleteTool(BaseTool):
    name = "strapi_delete"
    description = "Tool for strapi delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the strapi delete operation."""
        # Implement the tool logic here
        return f"Running strapi delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strapi delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
