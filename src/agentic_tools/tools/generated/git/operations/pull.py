from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitPullToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitPullTool(BaseTool):
    name: str = "git_pull"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git pull operation - pull operation"
    args_schema: type[BaseModel] | None = GitPullToolInput
    credentials: Optional[GitCredentials] = None
