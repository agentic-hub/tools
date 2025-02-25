from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglechatCreateToolInput(BaseModel):
    messageUi: Optional[Dict[str, Any]] = Field(None, description="Message")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    jsonParameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    spaceId: Optional[str] = Field(None, description="Space resource name, in the form \"spaces/*\". Example: spaces/AAAAMpdlehY. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    messageId: Optional[str] = Field(None, description="Resource name of the message to be deleted, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")
    messageJson: Optional[str] = Field(None, description="Message input as JSON Object or JSON String")


class GooglechatCreateTool(BaseTool):
    name = "googlechat_create"
    description = "Tool for googleChat create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the googleChat create operation."""
        # Implement the tool logic here
        return f"Running googleChat create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleChat create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
