from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehiveCredentials(BaseModel):
    """Credentials for theHive authentication."""
    the_hive_api: Optional[Dict[str, Any]] = Field(None, description="theHiveApi")

class ThehiveGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ThehiveCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    flag: Optional[bool] = Field(None, description="Flag of the case default=false")
    description: Optional[str] = Field(None, description="Description of the alert")
    analyzers: Optional[str] = Field(None, description="analyzers")
    tlp: Optional[str] = Field(None, description="Traffict Light Protocol (TLP). Default=Amber.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="Case ID")
    tags: Optional[str] = Field(None, description="Case Tags")
    id: Optional[str] = Field(None, description="Title of the alert")
    operation: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Description of the observable in the context of the case")
    severity: Optional[str] = Field(None, description="Severity of the alert. Default=Medium.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    status: Optional[str] = Field(None, description="Status of the alert")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    start_date: Optional[str] = Field(None, description="Date and time of the begin of the case default=now")
    title: Optional[str] = Field(None, description="Title of the alert")


class ThehiveGetTool(BaseTool):
    name = "thehive_get"
    description = "Tool for theHive get operation - get operation"
    
    def __init__(self, credentials: Optional[ThehiveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the theHive get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running theHive get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running theHive get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHive get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
