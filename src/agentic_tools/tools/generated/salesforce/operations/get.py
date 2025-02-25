from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SalesforceCredentials(BaseModel):
    """Credentials for salesforce authentication."""
    salesforce_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="salesforceOAuth2Api")
    salesforce_jwt_api: Optional[Dict[str, Any]] = Field(None, description="salesforceJwtApi")

class SalesforceGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SalesforceCredentials] = Field(None, description="Custom credentials for authentication")
    external_id: Optional[str] = Field(None, description="The field to check to see if the lead already exists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="ID of user that needs to be fetched")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    case_id: Optional[str] = Field(None, description="ID of case that needs to be fetched")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of account that needs to be fetched")
    custom_fields_ui: Optional[Dict[str, Any]] = Field(None, description="Filter by custom fields")
    task_id: Optional[str] = Field(None, description="ID of task that needs to be fetched")
    lastname: Optional[str] = Field(None, description="Required. Last name of the lead. Limited to 80 characters.")
    name: Optional[str] = Field(None, description="Required. Last name of the opportunity. Limited to 80 characters.")
    opportunity_id: Optional[str] = Field(None, description="ID of opportunity that needs to be fetched")
    external_id_value: Optional[str] = Field(None, description="If this value exists in the 'match against' field, update the lead. Otherwise create a new one.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    custom_object: Optional[str] = Field(None, description="Name of the custom object. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="OAuth Authorization Flow")
    contact_id: Optional[str] = Field(None, description="ID of contact that needs to be fetched")
    title: Optional[str] = Field(None, description="Title of the note")
    lead_id: Optional[str] = Field(None, description="ID of Lead that needs to be fetched")
    attachment_id: Optional[str] = Field(None, description="ID of attachment that needs to be fetched")
    record_id: Optional[str] = Field(None, description="Record ID to be retrieved")


class SalesforceGetTool(BaseTool):
    name = "salesforce_get"
    description = "Tool for salesforce get operation - get operation"
    
    def __init__(self, credentials: Optional[SalesforceCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the salesforce get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running salesforce get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running salesforce get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the salesforce get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
