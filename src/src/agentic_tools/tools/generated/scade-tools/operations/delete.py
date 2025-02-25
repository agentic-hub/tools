from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Scade-toolsDeleteToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    workflowId: Optional[Dict[str, Any]] = Field(None, description="Workflow to filter the executions by")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    workflowObject: Optional[str] = Field(None, description="A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href=\"https://docs.n8n.io/api/api-reference/#tag/Workflow/paths/~1workflows/post\">documentation</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    credentialTypeName: Optional[str] = Field(None, description="The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.")
    credentialId: Optional[str] = Field(None, description="Credential ID")
    executionId: Optional[str] = Field(None, description="Execution ID")
    additionalOptions: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    operation: Optional[str] = Field(None, description="Operation")


class Scade-toolsDeleteTool(BaseTool):
    name = "scade-tools_delete"
    description = "Tool for scade-tools delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the scade-tools delete operation."""
        # Implement the tool logic here
        return f"Running scade-tools delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the scade-tools delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
