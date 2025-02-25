from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplunkDeleteToolInput(BaseModel):
    searchConfigurationId: Optional[str] = Field(None, description="ID of the search configuration to delete")
    userId: Optional[str] = Field(None, description="ID of the user to delete")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    searchJobId: Optional[str] = Field(None, description="ID of the search job to delete")
    roles: Optional[str] = Field(None, description="roles")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkDeleteTool(BaseTool):
    name = "splunk_delete"
    description = "Tool for splunk delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the splunk delete operation."""
        # Implement the tool logic here
        return f"Running splunk delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the splunk delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
