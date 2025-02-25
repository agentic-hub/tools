from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DeeplCredentials(BaseModel):
    """Credentials for deepL authentication."""
    deep_l_api: Optional[Dict[str, Any]] = Field(None, description="deepLApi")

class DeeplTranslateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DeeplCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    translate_to: Optional[str] = Field(None, description="Language to translate to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="Input text to translate")
    operation: Optional[str] = Field(None, description="Operation")


class DeeplTranslateTool(BaseTool):
    name = "deepl_translate"
    description = "Tool for deepL translate operation - translate operation"
    
    def __init__(self, credentials: Optional[DeeplCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the deepL translate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running deepL translate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running deepL translate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the deepL translate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
