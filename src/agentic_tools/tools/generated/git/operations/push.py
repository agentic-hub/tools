from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitPushToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    operation: Optional[str] = Field(None, description="Operation")


class GitPushTool(BaseTool):
    name: str = "git_push"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git push operation - push operation"
    args_schema: type[BaseModel] | None = GitPushToolInput
    credentials: Optional[GitCredentials] = None
