from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ClockifyGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    taskId: Optional[str] = Field(None, description="ID of task to get")
    name: Optional[str] = Field(None, description="Name of client being created")
    clientId: Optional[str] = Field(None, description="Client ID")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    tagId: Optional[str] = Field(None, description="Tag ID")
    projectId: Optional[str] = Field(None, description="Project ID")
    workspaceId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    timeEntryId: Optional[str] = Field(None, description="Time Entry ID")


class ClockifyGetTool(BaseTool):
    name = "clockify_get"
    description = "Tool for clockify get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the clockify get operation."""
        # Implement the tool logic here
        return f"Running clockify get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the clockify get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
