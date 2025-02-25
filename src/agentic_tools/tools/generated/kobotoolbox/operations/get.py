from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KobotoolboxCredentials(BaseModel):
    """Credentials for koBoToolbox authentication."""
    ko_bo_toolbox_api: Optional[Dict[str, Any]] = Field(None, description="koBoToolboxApi")

class KobotoolboxGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[KobotoolboxCredentials] = Field(None, description="Custom credentials for authentication")
    file_id: Optional[str] = Field(None, description="Uid of the file (should start with \"af\" e.g. \"afQoJxA4kmKEXVpkH6SYbhb\"")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property to write the file into")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    download: Optional[bool] = Field(None, description="Whether to download the file content into a binary property")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    hook_id: Optional[str] = Field(None, description="Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)")
    resource: Optional[str] = Field(None, description="Resource")
    submission_id: Optional[str] = Field(None, description="Submission ID (number, e.g. 245128)")


class KobotoolboxGetTool(BaseTool):
    name = "kobotoolbox_get"
    description = "Tool for koBoToolbox get operation - get operation"
    
    def __init__(self, credentials: Optional[KobotoolboxCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the koBoToolbox get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running koBoToolbox get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running koBoToolbox get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the koBoToolbox get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
