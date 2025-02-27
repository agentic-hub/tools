from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GitCredentials

class GitTagToolInput(BaseModel):
    repository_path: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    name: Optional[str] = Field(None, description="The name of the tag to create")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitTagTool(BaseTool):
    name: str = "git_tag"
    connector_id: str = "nodes-base.git"
    description: str = "Tool for git tag operation - tag operation"
    args_schema: type[BaseModel] | None = GitTagToolInput
    credentials: Optional[GitCredentials] = None
