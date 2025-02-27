from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitAddconfigToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    value: Optional[str] = Field(None, description="Value of the key to set")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    key: Optional[str] = Field(None, description="Name of the key to set")
    operation: Optional[str] = Field(None, description="Operation")


class GitAddconfigTool(BaseTool):
    name: str = "git_addconfig"
    description: str = "Tool for git addConfig operation - addConfig operation"
    args_schema: type[BaseModel] | None = GitAddconfigToolInput
    credentials: Optional[GitCredentials] = None
