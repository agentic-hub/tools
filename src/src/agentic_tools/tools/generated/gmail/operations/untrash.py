from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GmailUntrashToolInput(BaseModel):
    threadId: Optional[str] = Field(None, description="The ID of the thread you are operating on")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subject: Optional[str] = Field(None, description="Subject")
    operation: Optional[str] = Field(None, description="Operation")
    emailType: Optional[str] = Field(None, description="Email Type")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    messageId: Optional[str] = Field(None, description="Draft ID")
    filtersNotice: Optional[str] = Field(None, description="Fetching a lot of messages may take a long time. Consider using filters to speed things up")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labelIds: Optional[str] = Field(None, description="labelIds")


class GmailUntrashTool(BaseTool):
    name = "gmail_untrash"
    description = "Tool for gmail untrash operation - untrash operation"
    
    def _run(self, **kwargs):
        """Run the gmail untrash operation."""
        # Implement the tool logic here
        return f"Running gmail untrash operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gmail untrash operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
