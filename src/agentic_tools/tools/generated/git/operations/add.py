from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitAddToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    paths_to_add: Optional[str] = Field(None, description="Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to add")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitAddTool(BaseTool):
    name: str = "git_add"
    description: str = "Tool for git add operation - add operation"
    args_schema: type[BaseModel] | None = GitAddToolInput
    credentials: Optional[GitCredentials] = None
