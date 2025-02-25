from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TaigaDeleteToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    projectId: Optional[str] = Field(None, description="ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    issueId: Optional[str] = Field(None, description="ID of the issue to delete")
    operation: Optional[str] = Field(None, description="Operation")
    userStoryId: Optional[str] = Field(None, description="ID of the user story to delete")
    epicId: Optional[str] = Field(None, description="ID of the epic to delete")


class TaigaDeleteTool(BaseTool):
    name = "taiga_delete"
    description = "Tool for taiga delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the taiga delete operation."""
        # Implement the tool logic here
        return f"Running taiga delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the taiga delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
