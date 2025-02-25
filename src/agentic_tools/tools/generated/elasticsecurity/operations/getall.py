from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsecurityGetallToolInput(BaseModel):
    commentId: Optional[str] = Field(None, description="ID of the case comment to retrieve")
    sortOptions: Optional[Dict[str, Any]] = Field(None, description="Sort")
    tag: Optional[str] = Field(None, description="Tag to attach to the case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    caseId: Optional[str] = Field(None, description="Case ID")
    connectorType: Optional[str] = Field(None, description="Connector Type")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    comment: Optional[str] = Field(None, description="Comment")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ElasticsecurityGetallTool(BaseTool):
    name = "elasticsecurity_getall"
    description = "Tool for elasticSecurity getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the elasticSecurity getAll operation."""
        # Implement the tool logic here
        return f"Running elasticSecurity getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticSecurity getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
