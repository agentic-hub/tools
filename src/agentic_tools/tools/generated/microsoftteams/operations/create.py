from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftteamsCredentials

class MicrosoftteamsCreateToolInput(BaseModel):
    team_id: Optional[Dict[str, Any]] = Field(None, description="Select the team from the list, by URL, or by ID (the ID is the \"groupId\" parameter in the URL you get from \"Get a link to the team\")")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel from the list, by URL, or by ID (the ID is the \"threadId\" in the URL)")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The ID of the task to delete")
    name: Optional[str] = Field(None, description="The name of the new channel you want to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    plan_id: Optional[Dict[str, Any]] = Field(None, description="The plan for the task to belong to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The content of the message to be sent")
    chat_id: Optional[Dict[str, Any]] = Field(None, description="Select the chat from the list, by URL, or by ID (find the chat ID after \"conversations/\" in the URL)")
    content_type: Optional[str] = Field(None, description="Whether the message is plain text or HTML")
    group_id: Optional[Dict[str, Any]] = Field(None, description="Team")
    bucket_id: Optional[str] = Field(None, description="By ID")
    resource: Optional[str] = Field(None, description="Resource")
    title: Optional[str] = Field(None, description="Title of the task")


class MicrosoftteamsCreateTool(BaseTool):
    name: str = "microsoftteams_create"
    connector_id: str = "nodes-base.microsoftTeams"
    description: str = "Tool for microsoftTeams create operation - create operation"
    args_schema: type[BaseModel] | None = MicrosoftteamsCreateToolInput
    credentials: Optional[MicrosoftteamsCredentials] = None
