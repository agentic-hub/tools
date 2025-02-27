from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GraphqlCredentials

class GraphqlDefaultToolInput(BaseModel):
    variables: Optional[str] = Field(None, description="Query variables")
    header_parameters_ui: Optional[Dict[str, Any]] = Field(None, description="The headers to send")
    request_method: Optional[str] = Field(None, description="The underlying HTTP request method to use")
    endpoint: Optional[str] = Field(None, description="The GraphQL endpoint")
    request_format: Optional[str] = Field(None, description="The format for the query payload")
    operation_name: Optional[str] = Field(None, description="Name of operation to execute")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    query: Optional[str] = Field(None, description="GraphQL query")
    allow_unauthorized_certs: Optional[bool] = Field(None, description="Whether to download the response even if SSL certificate validation is not possible")
    data_property_name: Optional[str] = Field(None, description="Name of the property to which to write the response data")
    response_format: Optional[str] = Field(None, description="The format in which the data gets returned from the URL")


class GraphqlDefaultTool(BaseTool):
    name: str = "graphql_default"
    connector_id: str = "nodes-base.graphql"
    description: str = "Tool for graphql default operation - default operation"
    args_schema: type[BaseModel] | None = GraphqlDefaultToolInput
    credentials: Optional[GraphqlCredentials] = None
