from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DisqusCredentials

class DisqusGetcategoriesToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The short name(aka ID) of the forum to get Categories")
    operation: Optional[str] = Field(None, description="Operation")


class DisqusGetcategoriesTool(BaseTool):
    name: str = "disqus_getcategories"
    connector_id: str = "nodes-base.disqus"
    description: str = "Tool for disqus getCategories operation - getCategories operation"
    args_schema: type[BaseModel] | None = DisqusGetcategoriesToolInput
    credentials: Optional[DisqusCredentials] = None
