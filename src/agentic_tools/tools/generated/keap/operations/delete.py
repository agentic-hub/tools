from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KeapCredentials(BaseModel):
    """Credentials for keap authentication."""
    keap_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="keapOAuth2Api")

class KeapDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[KeapCredentials] = Field(None, description="Custom credentials for authentication")
    file_id: Optional[str] = Field(None, description="File ID")
    tag_ids: Optional[str] = Field(None, description="tagIds")
    user_id: Optional[str] = Field(None, description="The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addresses_ui: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    order_id: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")
    faxes_ui: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    product_id: Optional[str] = Field(None, description="Product ID")


class KeapDeleteTool(BaseTool):
    name = "keap_delete"
    description = "Tool for keap delete operation - delete operation"
    
    def __init__(self, credentials: Optional[KeapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the keap delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running keap delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running keap delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the keap delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
