from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehiveCredentials(BaseModel):
    """Credentials for theHive authentication."""
    the_hive_api: Optional[Dict[str, Any]] = Field(None, description="theHiveApi")

class ThehiveCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ThehiveCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    data: Optional[str] = Field(None, description="Data")
    sighted: Optional[bool] = Field(None, description="Whether sighted previously")
    flag: Optional[bool] = Field(None, description="Flag of the case default=false")
    description: Optional[str] = Field(None, description="Description of the alert")
    analyzers: Optional[str] = Field(None, description="analyzers")
    tlp: Optional[str] = Field(None, description="Traffict Light Protocol (TLP). Default=Amber.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    type: Optional[str] = Field(None, description="Type of the alert")
    date: Optional[str] = Field(None, description="Date and time when the alert was raised default=now")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="ID of the case")
    tags: Optional[str] = Field(None, description="Case Tags")
    binary_property: Optional[str] = Field(None, description="The name of the input binary field that represent the attachment file")
    id: Optional[str] = Field(None, description="Title of the alert")
    operation: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    task_id: Optional[str] = Field(None, description="ID of the task")
    artifact_ui: Optional[Dict[str, Any]] = Field(None, description="Artifact attributes")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Description of the observable in the context of the case")
    severity: Optional[str] = Field(None, description="Severity of the alert. Default=Medium.")
    data_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Source of the alert")
    resource: Optional[str] = Field(None, description="Resource")
    follow: Optional[bool] = Field(None, description="Whether the alert becomes active when updated default=true")
    status: Optional[str] = Field(None, description="Status of the alert")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    ioc: Optional[bool] = Field(None, description="Whether the observable is an IOC (Indicator of compromise)")
    source_ref: Optional[str] = Field(None, description="Source reference of the alert")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    start_date: Optional[str] = Field(None, description="Date and time of the begin of the case default=now")
    title: Optional[str] = Field(None, description="Title of the alert")
    owner: Optional[str] = Field(None, description="Owner")


class ThehiveCreateTool(BaseTool):
    name = "thehive_create"
    description = "Tool for theHive create operation - create operation"
    
    def __init__(self, credentials: Optional[ThehiveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the theHive create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running theHive create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running theHive create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHive create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
