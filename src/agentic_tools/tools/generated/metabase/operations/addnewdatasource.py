from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MetabaseCredentials(BaseModel):
    """Credentials for metabase authentication."""
    metabase_api: Optional[Dict[str, Any]] = Field(None, description="metabaseApi")

class MetabaseAddnewdatasourceToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MetabaseCredentials] = Field(None, description="Custom credentials for authentication")
    file_path: Optional[str] = Field(None, description="File Path")
    full_sync: Optional[bool] = Field(None, description="Full Sync")
    password: Optional[str] = Field(None, description="Password")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    db_name: Optional[str] = Field(None, description="Database Name")
    engine: Optional[str] = Field(None, description="Engine")
    port: Optional[float] = Field(None, description="Port")
    host: Optional[str] = Field(None, description="Host")
    resource: Optional[str] = Field(None, description="Resource")
    user: Optional[str] = Field(None, description="User")


class MetabaseAddnewdatasourceTool(BaseTool):
    name = "metabase_addnewdatasource"
    description = "Tool for metabase addNewDatasource operation - addNewDatasource operation"
    
    def __init__(self, credentials: Optional[MetabaseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the metabase addNewDatasource operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running metabase addNewDatasource operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running metabase addNewDatasource operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the metabase addNewDatasource operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
