from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitUsersetupToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitUsersetupTool(BaseTool):
    name: str = "git_usersetup"
    description: str = "Tool for git userSetup operation - userSetup operation"
    args_schema: type[BaseModel] | None = GitUsersetupToolInput
    credentials: Optional[GitCredentials] = None
