from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GristCredentials(BaseModel):
    """Credentials for grist authentication."""
    grist_api: Optional[Dict[str, Any]] = Field(None, description="gristApi")

class GristGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GristCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    row_id: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristGetallTool(BaseTool):
    name = "grist_getall"
    description = "Tool for grist getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GristCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the grist getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running grist getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running grist getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grist getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
