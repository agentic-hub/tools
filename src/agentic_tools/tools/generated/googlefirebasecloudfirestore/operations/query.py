from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglefirebasecloudfirestoreCredentials(BaseModel):
    """Credentials for googleFirebaseCloudFirestore authentication."""
    google_firebase_cloud_firestore_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleFirebaseCloudFirestoreOAuth2Api")

class GooglefirebasecloudfirestoreQueryToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglefirebasecloudfirestoreCredentials] = Field(None, description="Custom credentials for authentication")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database: Optional[str] = Field(None, description="Usually the provided default value will work")
    collection: Optional[str] = Field(None, description="Collection name")
    query: Optional[str] = Field(None, description="JSON query to execute")
    document_id: Optional[str] = Field(None, description="Document ID")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="List of attributes to save")


class GooglefirebasecloudfirestoreQueryTool(BaseTool):
    name = "googlefirebasecloudfirestore_query"
    description = "Tool for googleFirebaseCloudFirestore query operation - query operation"
    
    def __init__(self, credentials: Optional[GooglefirebasecloudfirestoreCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleFirebaseCloudFirestore query operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleFirebaseCloudFirestore query operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleFirebaseCloudFirestore query operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleFirebaseCloudFirestore query operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
