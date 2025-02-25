from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UpleadEnrichToolInput(BaseModel):
    company: Optional[str] = Field(None, description="The name of the company (e.g – amazon)")
    lastname: Optional[str] = Field(None, description="Last name of the person (e.g – Benioff)")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address (e.g – mbenioff@salesforce.com)")
    firstname: Optional[str] = Field(None, description="First name of the person (e.g – Marc)")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name (e.g – amazon.com)")


class UpleadEnrichTool(BaseTool):
    name = "uplead_enrich"
    description = "Tool for uplead enrich operation - enrich operation"
    
    def _run(self, **kwargs):
        """Run the uplead enrich operation."""
        # Implement the tool logic here
        return f"Running uplead enrich operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the uplead enrich operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
