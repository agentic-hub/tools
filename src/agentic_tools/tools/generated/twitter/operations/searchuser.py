from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwitterSearchuserToolInput(BaseModel):
    tweetId: Optional[Dict[str, Any]] = Field(None, description="The tweet to like")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    noticeLocation: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    noticeAttachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    me: Optional[bool] = Field(None, description="Whether you want to search the authenticated user")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to search")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterSearchuserTool(BaseTool):
    name = "twitter_searchuser"
    description = "Tool for twitter searchUser operation - searchUser operation"
    
    def _run(self, **kwargs):
        """Run the twitter searchUser operation."""
        # Implement the tool logic here
        return f"Running twitter searchUser operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twitter searchUser operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
