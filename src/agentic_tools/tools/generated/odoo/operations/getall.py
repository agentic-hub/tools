from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OdooCredentials(BaseModel):
    """Credentials for odoo authentication."""
    odoo_api: Optional[Dict[str, Any]] = Field(None, description="odooApi")

class OdooGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OdooCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    custom_resource: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    custom_resource_id: Optional[str] = Field(None, description="Custom Resource ID")
    filter_request: Optional[Dict[str, Any]] = Field(None, description="Filter request by applying filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    memo: Optional[str] = Field(None, description="Memo")
    operation: Optional[str] = Field(None, description="Operation")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    fields_to_create_or_update: Optional[Dict[str, Any]] = Field(None, description="Fields")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")


class OdooGetallTool(BaseTool):
    name = "odoo_getall"
    description = "Tool for odoo getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[OdooCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the odoo getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running odoo getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running odoo getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the odoo getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
