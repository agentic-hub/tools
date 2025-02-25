from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwitterDeleteToolInput(BaseModel):
    tweetId: Optional[Dict[str, Any]] = Field(None, description="The tweet to like")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    noticeLocation: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    noticeAttachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to send the message to")
    tweetDeleteId: Optional[str] = Field(None, description="By ID")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterDeleteTool(BaseTool):
    name = "twitter_delete"
    description = "Tool for twitter delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the twitter delete operation."""
        # Implement the tool logic here
        return f"Running twitter delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twitter delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
