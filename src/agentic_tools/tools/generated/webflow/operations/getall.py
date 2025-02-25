from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WebflowGetallToolInput(BaseModel):
    live: Optional[bool] = Field(None, description="Whether the item should be published on the live site")
    itemId: Optional[str] = Field(None, description="ID of the item to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    siteId: Optional[str] = Field(None, description="ID of the site containing the collection whose items to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    collectionId: Optional[str] = Field(None, description="ID of the collection whose items to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields")


class WebflowGetallTool(BaseTool):
    name = "webflow_getall"
    description = "Tool for webflow getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the webflow getAll operation."""
        # Implement the tool logic here
        return f"Running webflow getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the webflow getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
