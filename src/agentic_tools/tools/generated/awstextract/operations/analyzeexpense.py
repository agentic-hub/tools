from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstextractCredentials(BaseModel):
    """Credentials for awsTextract authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwstextractAnalyzeexpenseToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwstextractCredentials] = Field(None, description="Custom credentials for authentication")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    binary_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded. Supported file types: PNG, JPEG.")
    operation: Optional[str] = Field(None, description="Operation")


class AwstextractAnalyzeexpenseTool(BaseTool):
    name = "awstextract_analyzeexpense"
    description = "Tool for awsTextract analyzeExpense operation - analyzeExpense operation"
    
    def __init__(self, credentials: Optional[AwstextractCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsTextract analyzeExpense operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsTextract analyzeExpense operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsTextract analyzeExpense operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTextract analyzeExpense operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
