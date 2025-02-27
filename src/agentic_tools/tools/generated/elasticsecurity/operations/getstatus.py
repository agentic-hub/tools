from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ElasticsecurityCredentials

class ElasticsecurityGetstatusToolInput(BaseModel):
    comment_id: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="Case ID")
    connector_type: Optional[str] = Field(None, description="Connector Type")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    comment: Optional[str] = Field(None, description="Comment")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ElasticsecurityGetstatusTool(BaseTool):
    name: str = "elasticsecurity_getstatus"
    connector_id: str = "nodes-base.elasticSecurity"
    description: str = "Tool for elasticSecurity getStatus operation - getStatus operation"
    args_schema: type[BaseModel] | None = ElasticsecurityGetstatusToolInput
    credentials: Optional[ElasticsecurityCredentials] = None
