from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AgilecrmCredentials(BaseModel):
    """Credentials for agileCrm authentication."""
    agile_crm_api: Optional[Dict[str, Any]] = Field(None, description="agileCrmApi")

class AgilecrmCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AgilecrmCredentials] = Field(None, description="Custom credentials for authentication")
    close_date: Optional[str] = Field(None, description="Closing date of deal")
    expected_value: Optional[float] = Field(None, description="Expected Value of deal")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter\" target=\"_blank\">Agile CRM guide</a> to creating filters")
    probability: Optional[float] = Field(None, description="Expected probability")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-contacts---companies-api\">here</a>")
    company_id: Optional[str] = Field(None, description="Unique identifier for a particular company")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of deal")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    milestone: Optional[str] = Field(None, description="Milestone of deal")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[str] = Field(None, description="Unique identifier for a particular deal")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    filter_type: Optional[str] = Field(None, description="Filter")
    match_type: Optional[str] = Field(None, description="Must Match")


class AgilecrmCreateTool(BaseTool):
    name = "agilecrm_create"
    description = "Tool for agileCrm create operation - create operation"
    
    def __init__(self, credentials: Optional[AgilecrmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the agileCrm create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running agileCrm create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running agileCrm create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the agileCrm create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
