from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KobotoolboxCredentials(BaseModel):
    """Credentials for koBoToolbox authentication."""
    ko_bo_toolbox_api: Optional[Dict[str, Any]] = Field(None, description="koBoToolboxApi")

class KobotoolboxGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[KobotoolboxCredentials] = Field(None, description="Custom credentials for authentication")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters\" target=\"_blank\">Formhub API docs</a> to creating filters, using the MongoDB JSON format - e.g. {\"_submission_time\":{\"$lt\":\"2021-10-01T01:02:03\"}}")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property to write the file into")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    filter_type: Optional[str] = Field(None, description="Filter")


class KobotoolboxGetallTool(BaseTool):
    name = "kobotoolbox_getall"
    description = "Tool for koBoToolbox getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[KobotoolboxCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the koBoToolbox getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running koBoToolbox getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running koBoToolbox getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the koBoToolbox getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
