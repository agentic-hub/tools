from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftteamsGetToolInput(BaseModel):
    teamId: Optional[Dict[str, Any]] = Field(None, description="Select the team from the list, by URL, or by ID (the ID is the \"groupId\" parameter in the URL you get from \"Get a link to the team\")")
    channelId: Optional[Dict[str, Any]] = Field(None, description="Select the channel from the list, by URL, or by ID (the ID is the \"threadId\" in the URL)")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="The ID of the task to retrieve")
    name: Optional[str] = Field(None, description="The name of the new channel you want to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    planId: Optional[Dict[str, Any]] = Field(None, description="The plan for the task to belong to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The content of the message to be sent")
    chatId: Optional[Dict[str, Any]] = Field(None, description="Select the chat from the list, by URL, or by ID (find the chat ID after \"conversations/\" in the URL)")
    contentType: Optional[str] = Field(None, description="Whether the message is plain text or HTML")
    groupId: Optional[Dict[str, Any]] = Field(None, description="Team")
    messageId: Optional[str] = Field(None, description="The ID of the message to retrieve")
    resource: Optional[str] = Field(None, description="Resource")


class MicrosoftteamsGetTool(BaseTool):
    name = "microsoftteams_get"
    description = "Tool for microsoftTeams get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the microsoftTeams get operation."""
        # Implement the tool logic here
        return f"Running microsoftTeams get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftTeams get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
