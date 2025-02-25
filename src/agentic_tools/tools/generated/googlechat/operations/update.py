from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglechatUpdateToolInput(BaseModel):
    updateFieldsUi: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    updateFieldsJson: Optional[str] = Field(None, description="Message input as JSON Object or JSON String")
    jsonParameters: Optional[bool] = Field(None, description="Whether to pass the update fields object as JSON")
    spaceId: Optional[str] = Field(None, description="The name of the space for which to retrieve members, in the form \"spaces/*\". Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    messageId: Optional[str] = Field(None, description="Resource name of the message to be updated, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatUpdateTool(BaseTool):
    name = "googlechat_update"
    description = "Tool for googleChat update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the googleChat update operation."""
        # Implement the tool logic here
        return f"Running googleChat update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleChat update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
