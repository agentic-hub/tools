from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitCloneToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    source_repository: Optional[str] = Field(None, description="The URL or path of the repository to clone")
    operation: Optional[str] = Field(None, description="Operation")


class GitCloneTool(BaseTool):
    name: str = "git_clone"
    description: str = "Tool for git clone operation - clone operation"
    args_schema: type[BaseModel] | None = GitCloneToolInput
    credentials: Optional[GitCredentials] = None
