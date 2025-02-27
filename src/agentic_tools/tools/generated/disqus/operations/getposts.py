from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DisqusCredentials

class DisqusGetpostsToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The short name(aka ID) of the forum to get")
    operation: Optional[str] = Field(None, description="Operation")


class DisqusGetpostsTool(BaseTool):
    name: str = "disqus_getposts"
    connector_id: str = "nodes-base.disqus"
    description: str = "Tool for disqus getPosts operation - getPosts operation"
    args_schema: type[BaseModel] | None = DisqusGetpostsToolInput
    credentials: Optional[DisqusCredentials] = None
