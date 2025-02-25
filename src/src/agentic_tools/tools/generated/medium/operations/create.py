from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MediumCreateToolInput(BaseModel):
    publication: Optional[bool] = Field(None, description="Whether you are posting for a publication")
    content: Optional[str] = Field(None, description="The body of the post, in a valid semantic HTML fragment, or Markdown")
    resource: Optional[str] = Field(None, description="Resource")
    publicationId: Optional[str] = Field(None, description="Publication IDs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the post. Max Length : 100 characters.")
    contentFormat: Optional[str] = Field(None, description="The format of the content to be posted")
    operation: Optional[str] = Field(None, description="Operation")


class MediumCreateTool(BaseTool):
    name = "medium_create"
    description = "Tool for medium create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the medium create operation."""
        # Implement the tool logic here
        return f"Running medium create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the medium create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
