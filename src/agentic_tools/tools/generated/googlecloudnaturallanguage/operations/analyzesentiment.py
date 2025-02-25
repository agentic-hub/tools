from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecloudnaturallanguageCredentials(BaseModel):
    """Credentials for googleCloudNaturalLanguage authentication."""
    google_cloud_natural_language_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCloudNaturalLanguageOAuth2Api")

class GooglecloudnaturallanguageAnalyzesentimentToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecloudnaturallanguageCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The content of the input in string format. Cloud audit logging exempt since it is based on user data.")
    source: Optional[str] = Field(None, description="The source of the document: a string containing the content or a Google Cloud Storage URI")
    resource: Optional[str] = Field(None, description="Resource")
    gcs_content_uri: Optional[str] = Field(None, description="The Google Cloud Storage URI where the file content is located. This URI must be of the form: <code>gs://bucket_name/object_name</code>. For more details, see <a href=\"https://cloud.google.com/storage/docs/reference-uris.\">reference</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecloudnaturallanguageAnalyzesentimentTool(BaseTool):
    name = "googlecloudnaturallanguage_analyzesentiment"
    description = "Tool for googleCloudNaturalLanguage analyzeSentiment operation - analyzeSentiment operation"
    
    def __init__(self, credentials: Optional[GooglecloudnaturallanguageCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleCloudNaturalLanguage analyzeSentiment operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleCloudNaturalLanguage analyzeSentiment operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleCloudNaturalLanguage analyzeSentiment operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleCloudNaturalLanguage analyzeSentiment operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
