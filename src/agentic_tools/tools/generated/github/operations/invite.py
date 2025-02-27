from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GithubCredentials

class GithubInviteToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="The file path of the file. Has to contain the full path.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organization: Optional[str] = Field(None, description="The GitHub organization that the user is being invited to")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    email: Optional[str] = Field(None, description="The email address of the invited user")
    issue_number: Optional[float] = Field(None, description="The number of the issue on which to create the comment on")
    operation: Optional[str] = Field(None, description="Operation")
    pull_request_number: Optional[float] = Field(None, description="The number of the pull request")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    repository: Optional[str] = Field(None, description="Link")
    body: Optional[str] = Field(None, description="The body of the issue")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    additional_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    owner: Optional[str] = Field(None, description="Link")


class GithubInviteTool(BaseTool):
    name: str = "github_invite"
    description: str = "Tool for github invite operation - invite operation"
    args_schema: type[BaseModel] | None = GithubInviteToolInput
    credentials: Optional[GithubCredentials] = None
