from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LingvanexCredentials(BaseModel):
    """Credentials for lingvaNex authentication."""
    lingva_nex_api: Optional[Dict[str, Any]] = Field(None, description="lingvaNexApi")

class LingvanexTranslateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LingvanexCredentials] = Field(None, description="Custom credentials for authentication")
    translate_to: Optional[str] = Field(None, description="The language to use for translation of the input text, set to one of the language codes listed in <a href=\"https://cloud.google.com/translate/docs/languages\">Language Support</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    text: Optional[str] = Field(None, description="The input text to translate")
    operation: Optional[str] = Field(None, description="Operation")


class LingvanexTranslateTool(BaseTool):
    name = "lingvanex_translate"
    description = "Tool for lingvaNex translate operation - translate operation"
    
    def __init__(self, credentials: Optional[LingvanexCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the lingvaNex translate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running lingvaNex translate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running lingvaNex translate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the lingvaNex translate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
