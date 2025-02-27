from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitLogToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitLogTool(BaseTool):
    name: str = "git_log"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git log operation - log operation"
    args_schema: type[BaseModel] | None = GitLogToolInput
    credentials: Optional[GitCredentials] = None
