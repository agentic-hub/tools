from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftteamsCredentials

class MicrosoftteamsUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    team_id: Optional[Dict[str, Any]] = Field(None, description="Select the team from the list, by URL, or by ID (the ID is the \"groupId\" parameter in the URL you get from \"Get a link to the team\")")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel from the list, by URL, or by ID (the ID is the \"threadId\" in the URL)")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The ID of the task to update")
    name: Optional[str] = Field(None, description="The name of the channel")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    plan_id: Optional[Dict[str, Any]] = Field(None, description="The plan for the task to belong to")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The content of the message to be sent")
    chat_id: Optional[Dict[str, Any]] = Field(None, description="Select the chat from the list, by URL, or by ID (find the chat ID after \"conversations/\" in the URL)")
    content_type: Optional[str] = Field(None, description="Whether the message is plain text or HTML")
    group_id: Optional[Dict[str, Any]] = Field(None, description="Team")
    resource: Optional[str] = Field(None, description="Resource")


class MicrosoftteamsUpdateTool(BaseTool):
    name: str = "microsoftteams_update"
    connector_id: str = "nodes-base.microsoftTeams"
    description: str = "Tool for microsoftTeams update operation - update operation"
    args_schema: type[BaseModel] | None = MicrosoftteamsUpdateToolInput
    credentials: Optional[MicrosoftteamsCredentials] = None
