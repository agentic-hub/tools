from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitPushtagsToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitPushtagsTool(BaseTool):
    name: str = "git_pushtags"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git pushTags operation - pushTags operation"
    args_schema: type[BaseModel] | None = GitPushtagsToolInput
    credentials: Optional[GitCredentials] = None
