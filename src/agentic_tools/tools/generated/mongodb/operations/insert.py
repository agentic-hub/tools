from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MongodbCredentials(BaseModel):
    """Credentials for mongoDb authentication."""
    mongo_db: Optional[Dict[str, Any]] = Field(None, description="mongoDb")

class MongodbInsertToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MongodbCredentials] = Field(None, description="Custom credentials for authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbInsertTool(BaseTool):
    name = "mongodb_insert"
    description = "Tool for mongoDb insert operation - insert operation"
    
    def __init__(self, credentials: Optional[MongodbCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mongoDb insert operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mongoDb insert operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mongoDb insert operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mongoDb insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
