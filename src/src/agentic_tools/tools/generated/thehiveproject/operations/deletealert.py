from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehiveprojectDeletealertToolInput(BaseModel):
    sort: Optional[Dict[str, Any]] = Field(None, description="Sort")
    content: Optional[str] = Field(None, description="Content")
    location: Optional[str] = Field(None, description="Create in")
    observableFields: Optional[str] = Field(None, description="observableFields")
    pageId: Optional[Dict[str, Any]] = Field(None, description="Page")
    commentId: Optional[Dict[str, Any]] = Field(None, description="Comment")
    analyzers: Optional[str] = Field(None, description="analyzers")
    alertId: Optional[Dict[str, Any]] = Field(None, description="Alert")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    observableId: Optional[Dict[str, Any]] = Field(None, description="Observable")
    caseId: Optional[Dict[str, Any]] = Field(None, description="Case")
    taskUpdateFields: Optional[str] = Field(None, description="taskUpdateFields")
    alertFields: Optional[str] = Field(None, description="alertFields")
    id: Optional[Dict[str, Any]] = Field(None, description="Alert")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[Dict[str, Any]] = Field(None, description="Task")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    taskFields: Optional[str] = Field(None, description="taskFields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    alertUpdateFields: Optional[str] = Field(None, description="alertUpdateFields")
    dataType: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    searchIn: Optional[str] = Field(None, description="Whether to search for comments in all alerts and cases or in a specific case or alert")
    resource: Optional[str] = Field(None, description="Resource")
    caseUpdateFields: Optional[str] = Field(None, description="caseUpdateFields")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attachmentsUi: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    caseFields: Optional[str] = Field(None, description="caseFields")
    logId: Optional[Dict[str, Any]] = Field(None, description="Task Log")
    observableUpdateFields: Optional[str] = Field(None, description="observableUpdateFields")
    logFields: Optional[str] = Field(None, description="logFields")
    attachmentId: Optional[str] = Field(None, description="ID of the attachment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ThehiveprojectDeletealertTool(BaseTool):
    name = "thehiveproject_deletealert"
    description = "Tool for theHiveProject deleteAlert operation - deleteAlert operation"
    
    def _run(self, **kwargs):
        """Run the theHiveProject deleteAlert operation."""
        # Implement the tool logic here
        return f"Running theHiveProject deleteAlert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHiveProject deleteAlert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
