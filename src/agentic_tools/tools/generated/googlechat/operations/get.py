from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglechatGetToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    memberId: Optional[str] = Field(None, description="Member to be retrieved in the form \"spaces/*/members/*\"")
    jsonParameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    spaceId: Optional[str] = Field(None, description="Resource name of the space, in the form \"spaces/*\"")
    messageId: Optional[str] = Field(None, description="Resource name of the message to be retrieved, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatGetTool(BaseTool):
    name = "googlechat_get"
    description = "Tool for googleChat get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the googleChat get operation."""
        # Implement the tool logic here
        return f"Running googleChat get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleChat get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
