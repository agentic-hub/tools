from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitFetchToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitFetchTool(BaseTool):
    name: str = "git_fetch"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git fetch operation - fetch operation"
    args_schema: type[BaseModel] | None = GitFetchToolInput
    credentials: Optional[GitCredentials] = None
