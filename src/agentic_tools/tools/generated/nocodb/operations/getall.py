from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NocodbCredentials(BaseModel):
    """Credentials for nocoDb authentication."""
    noco_db: Optional[Dict[str, Any]] = Field(None, description="nocoDb")
    noco_db_api_token: Optional[Dict[str, Any]] = Field(None, description="nocoDbApiToken")

class NocodbGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[NocodbCredentials] = Field(None, description="Custom credentials for authentication")
    table: Optional[str] = Field(None, description="The table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    primary_key: Optional[str] = Field(None, description="Primary Key Type")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    id: Optional[str] = Field(None, description="The value of the ID field")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    download_field_names: Optional[str] = Field(None, description="Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    version: Optional[str] = Field(None, description="API Version")
    custom_primary_key: Optional[str] = Field(None, description="Field Name")
    resource: Optional[str] = Field(None, description="Resource")
    download_attachments: Optional[bool] = Field(None, description="Whether the attachment fields define in 'Download Fields' will be downloaded")
    project_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    authentication: Optional[str] = Field(None, description="Authentication")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in NocoDB. (Use an 'Edit Fields' node before this node to change them if required.)")


class NocodbGetallTool(BaseTool):
    name = "nocodb_getall"
    description = "Tool for nocoDb getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[NocodbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the nocoDb getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running nocoDb getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running nocoDb getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nocoDb getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
