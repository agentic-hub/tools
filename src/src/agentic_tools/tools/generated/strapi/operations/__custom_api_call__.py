from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Strapi__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entryId: Optional[str] = Field(None, description="The ID of the entry to delete")
    contentType: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class Strapi__custom_api_call__Tool(BaseTool):
    name = "strapi___custom_api_call__"
    description = "Tool for strapi __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the strapi __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running strapi __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strapi __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
