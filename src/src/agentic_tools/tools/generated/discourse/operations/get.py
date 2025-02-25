from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DiscourseGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post")
    externalId: Optional[str] = Field(None, description="Discourse SSO external ID")
    postId: Optional[str] = Field(None, description="ID of the post")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    operation: Optional[str] = Field(None, description="Choose an operation")
    name: Optional[str] = Field(None, description="Name of the group")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    by: Optional[str] = Field(None, description="What to search by")
    username: Optional[str] = Field(None, description="The username of the user to return")
    groupId: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class DiscourseGetTool(BaseTool):
    name = "discourse_get"
    description = "Tool for discourse get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the discourse get operation."""
        # Implement the tool logic here
        return f"Running discourse get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the discourse get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
