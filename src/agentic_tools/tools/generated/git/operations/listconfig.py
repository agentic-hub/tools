from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitListconfigToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitListconfigTool(BaseTool):
    name: str = "git_listconfig"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git listConfig operation - listConfig operation"
    args_schema: type[BaseModel] | None = GitListconfigToolInput
    credentials: Optional[GitCredentials] = None
