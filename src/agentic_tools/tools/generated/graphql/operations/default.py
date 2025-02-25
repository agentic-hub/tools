from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GraphqlDefaultToolInput(BaseModel):
    variables: Optional[str] = Field(None, description="Query variables")
    headerParametersUi: Optional[Dict[str, Any]] = Field(None, description="The headers to send")
    requestMethod: Optional[str] = Field(None, description="The underlying HTTP request method to use")
    endpoint: Optional[str] = Field(None, description="The GraphQL endpoint")
    requestFormat: Optional[str] = Field(None, description="The format for the query payload")
    operationName: Optional[str] = Field(None, description="Name of operation to execute")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    query: Optional[str] = Field(None, description="GraphQL query")
    allowUnauthorizedCerts: Optional[bool] = Field(None, description="Whether to download the response even if SSL certificate validation is not possible")
    dataPropertyName: Optional[str] = Field(None, description="Name of the property to which to write the response data")
    responseFormat: Optional[str] = Field(None, description="The format in which the data gets returned from the URL")


class GraphqlDefaultTool(BaseTool):
    name = "graphql_default"
    description = "Tool for graphql default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the graphql default operation."""
        # Implement the tool logic here
        return f"Running graphql default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the graphql default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
