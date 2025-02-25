from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ServicenowCredentials(BaseModel):
    """Credentials for serviceNow authentication."""
    service_now_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="serviceNowOAuth2Api")
    service_now_basic_api: Optional[Dict[str, Any]] = Field(None, description="serviceNowBasicApi")

class ServicenowGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ServicenowCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    short_description: Optional[str] = Field(None, description="Short description of the incident")
    get_option: Optional[str] = Field(None, description="Unique identifier of the user")
    output_field: Optional[str] = Field(None, description="Field name where downloaded data will be placed")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all inputs.")
    id: Optional[str] = Field(None, description="Unique identifier of the incident")
    fields_to_send: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    operation: Optional[str] = Field(None, description="Operation")
    download: Optional[bool] = Field(None, description="Download Attachments")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    data_to_send: Optional[str] = Field(None, description="Data to Send")
    user_name: Optional[str] = Field(None, description="Unique identifier of the user")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication method to use")
    attachment_id: Optional[str] = Field(None, description="Sys_id value of the attachment to delete")
    table_name: Optional[str] = Field(None, description="Name of the table in which the record exists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ServicenowGetTool(BaseTool):
    name = "servicenow_get"
    description = "Tool for serviceNow get operation - get operation"
    
    def __init__(self, credentials: Optional[ServicenowCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the serviceNow get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running serviceNow get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running serviceNow get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the serviceNow get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
