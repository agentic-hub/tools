from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SecurityscorecardCredentials(BaseModel):
    """Credentials for securityScorecard authentication."""
    security_scorecard_api: Optional[Dict[str, Any]] = Field(None, description="securityScorecardApi")

class SecurityscorecardGenerateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SecurityscorecardCredentials] = Field(None, description="Custom credentials for authentication")
    branding: Optional[str] = Field(None, description="Branding")
    report: Optional[str] = Field(None, description="Report")
    date: Optional[str] = Field(None, description="Date")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    scorecard_identifier: Optional[str] = Field(None, description="Primary identifier of a company or scorecard, i.e. domain.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    portfolio_id: Optional[str] = Field(None, description="Portfolio ID")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")


class SecurityscorecardGenerateTool(BaseTool):
    name = "securityscorecard_generate"
    description = "Tool for securityScorecard generate operation - generate operation"
    
    def __init__(self, credentials: Optional[SecurityscorecardCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the securityScorecard generate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running securityScorecard generate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running securityScorecard generate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the securityScorecard generate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
