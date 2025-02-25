from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class InvoiceninjaCredentials(BaseModel):
    """Credentials for invoiceNinja authentication."""
    invoice_ninja_api: Optional[Dict[str, Any]] = Field(None, description="invoiceNinjaApi")

class InvoiceninjaGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[InvoiceninjaCredentials] = Field(None, description="Custom credentials for authentication")
    invoice_id: Optional[str] = Field(None, description="Invoice ID")
    invoice_items_ui: Optional[Dict[str, Any]] = Field(None, description="Invoice Items")
    expense_id: Optional[str] = Field(None, description="Expense ID")
    quote_id: Optional[str] = Field(None, description="Quote ID")
    payment_id: Optional[str] = Field(None, description="Payment ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    api_version: Optional[str] = Field(None, description="API Version")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class InvoiceninjaGetTool(BaseTool):
    name = "invoiceninja_get"
    description = "Tool for invoiceNinja get operation - get operation"
    
    def __init__(self, credentials: Optional[InvoiceninjaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the invoiceNinja get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running invoiceNinja get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running invoiceNinja get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the invoiceNinja get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
