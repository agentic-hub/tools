from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecontactsCredentials(BaseModel):
    """Credentials for googleContacts authentication."""
    google_contacts_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleContactsOAuth2Api")

class GooglecontactsGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecontactsCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    use_query: Optional[bool] = Field(None, description="Whether or not to use a query to filter the results")
    query: Optional[str] = Field(None, description="The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name \"foo name\" matches queries such as \"f\", \"fo\", \"foo\", \"foo n\", \"nam\", etc., but not \"oo n\".")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsGetallTool(BaseTool):
    name = "googlecontacts_getall"
    description = "Tool for googleContacts getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GooglecontactsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleContacts getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleContacts getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleContacts getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleContacts getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
