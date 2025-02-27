from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ElasticsecurityCredentials

class ElasticsecurityRemoveToolInput(BaseModel):
    comment_id: Optional[str] = Field(None, description="Comment ID")
    tag: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="ID of the case containing the comment to remove")
    connector_type: Optional[str] = Field(None, description="Connector Type")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    comment: Optional[str] = Field(None, description="Comment")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ElasticsecurityRemoveTool(BaseTool):
    name: str = "elasticsecurity_remove"
    connector_id: str = "nodes-base.elasticSecurity"
    description: str = "Tool for elasticSecurity remove operation - remove operation"
    args_schema: type[BaseModel] | None = ElasticsecurityRemoveToolInput
    credentials: Optional[ElasticsecurityCredentials] = None
