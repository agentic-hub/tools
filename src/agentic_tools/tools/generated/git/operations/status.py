from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitStatusToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitStatusTool(BaseTool):
    name: str = "git_status"
    description: str = "Tool for git status operation - status operation"
    args_schema: type[BaseModel] | None = GitStatusToolInput
    credentials: Optional[GitCredentials] = None
