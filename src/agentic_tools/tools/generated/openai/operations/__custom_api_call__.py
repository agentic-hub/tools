from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OpenaiCredentials(BaseModel):
    """Credentials for openAi authentication."""
    open_ai_api: Optional[Dict[str, Any]] = Field(None, description="openAiApi")

class Openai__custom_api_call__ToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OpenaiCredentials] = Field(None, description="Custom credentials for authentication")
    prompt: Optional[Dict[str, Any]] = Field(None, description="Prompt")
    simplify_output: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    input: Optional[str] = Field(None, description="The input text to be edited")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options to add")
    model: Optional[str] = Field(None, description="The model which will generate the completion. <a href=\"https://beta.openai.com/docs/models/overview\">Learn more</a>.")
    notice_advance_ai: Optional[str] = Field(None, description="For more advanced uses, consider using an <a data-action=\"openSelectiveNodeCreator\" data-action-parameter-creatorview=\"AI\">advanced AI</a> node")
    operation: Optional[str] = Field(None, description="Operation")


class Openai__custom_api_call__Tool(BaseTool):
    name = "openai___custom_api_call__"
    description = "Tool for openAi __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def __init__(self, credentials: Optional[OpenaiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the openAi __CUSTOM_API_CALL__ operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running openAi __CUSTOM_API_CALL__ operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running openAi __CUSTOM_API_CALL__ operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the openAi __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
