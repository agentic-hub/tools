from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitCommitToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The commit message to use")
    operation: Optional[str] = Field(None, description="Operation")


class GitCommitTool(BaseTool):
    name: str = "git_commit"
    description: str = "Tool for git commit operation - commit operation"
    args_schema: type[BaseModel] | None = GitCommitToolInput
    credentials: Optional[GitCredentials] = None
