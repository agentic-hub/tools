from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsecurityDeleteToolInput(BaseModel):
    commentId: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    caseId: Optional[str] = Field(None, description="Case ID")
    connectorType: Optional[str] = Field(None, description="Connector Type")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    comment: Optional[str] = Field(None, description="Comment")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ElasticsecurityDeleteTool(BaseTool):
    name = "elasticsecurity_delete"
    description = "Tool for elasticSecurity delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the elasticSecurity delete operation."""
        # Implement the tool logic here
        return f"Running elasticSecurity delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticSecurity delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
