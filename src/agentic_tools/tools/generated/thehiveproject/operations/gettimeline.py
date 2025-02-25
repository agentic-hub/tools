from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehiveprojectCredentials(BaseModel):
    """Credentials for theHiveProject authentication."""
    the_hive_project_api: Optional[Dict[str, Any]] = Field(None, description="theHiveProjectApi")

class ThehiveprojectGettimelineToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ThehiveprojectCredentials] = Field(None, description="Custom credentials for authentication")
    sort: Optional[Dict[str, Any]] = Field(None, description="Sort")
    content: Optional[str] = Field(None, description="Content")
    location: Optional[str] = Field(None, description="Create in")
    observable_fields: Optional[str] = Field(None, description="observableFields")
    page_id: Optional[Dict[str, Any]] = Field(None, description="Page")
    comment_id: Optional[Dict[str, Any]] = Field(None, description="Comment")
    analyzers: Optional[str] = Field(None, description="analyzers")
    alert_id: Optional[Dict[str, Any]] = Field(None, description="Alert")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    observable_id: Optional[Dict[str, Any]] = Field(None, description="Observable")
    case_id: Optional[Dict[str, Any]] = Field(None, description="Case")
    task_update_fields: Optional[str] = Field(None, description="taskUpdateFields")
    alert_fields: Optional[str] = Field(None, description="alertFields")
    id: Optional[Dict[str, Any]] = Field(None, description="Alert")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[Dict[str, Any]] = Field(None, description="Task")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    task_fields: Optional[str] = Field(None, description="taskFields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    alert_update_fields: Optional[str] = Field(None, description="alertUpdateFields")
    data_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    search_in: Optional[str] = Field(None, description="Whether to search for comments in all alerts and cases or in a specific case or alert")
    resource: Optional[str] = Field(None, description="Resource")
    case_update_fields: Optional[str] = Field(None, description="caseUpdateFields")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    case_fields: Optional[str] = Field(None, description="caseFields")
    log_id: Optional[Dict[str, Any]] = Field(None, description="Task Log")
    observable_update_fields: Optional[str] = Field(None, description="observableUpdateFields")
    log_fields: Optional[str] = Field(None, description="logFields")
    attachment_id: Optional[str] = Field(None, description="ID of the attachment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ThehiveprojectGettimelineTool(BaseTool):
    name = "thehiveproject_gettimeline"
    description = "Tool for theHiveProject getTimeline operation - getTimeline operation"
    
    def __init__(self, credentials: Optional[ThehiveprojectCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the theHiveProject getTimeline operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running theHiveProject getTimeline operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running theHiveProject getTimeline operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHiveProject getTimeline operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
