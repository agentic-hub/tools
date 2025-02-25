from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MetabaseCredentials(BaseModel):
    """Credentials for metabase authentication."""
    metabase_api: Optional[Dict[str, Any]] = Field(None, description="metabaseApi")

class MetabaseResultdataToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MetabaseCredentials] = Field(None, description="Custom credentials for authentication")
    format: Optional[str] = Field(None, description="Format")
    question_id: Optional[str] = Field(None, description="Question ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseResultdataTool(BaseTool):
    name = "metabase_resultdata"
    description = "Tool for metabase resultData operation - resultData operation"
    
    def __init__(self, credentials: Optional[MetabaseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the metabase resultData operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running metabase resultData operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running metabase resultData operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the metabase resultData operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
