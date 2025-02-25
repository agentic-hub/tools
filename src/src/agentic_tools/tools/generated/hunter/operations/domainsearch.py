from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HunterDomainsearchToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    onlyEmails: Optional[bool] = Field(None, description="Whether to return only the the found emails")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation to consume")
    domain: Optional[str] = Field(None, description="Domain name from which you want to find the email addresses. For example, \"stripe.com\".")


class HunterDomainsearchTool(BaseTool):
    name = "hunter_domainsearch"
    description = "Tool for hunter domainSearch operation - domainSearch operation"
    
    def _run(self, **kwargs):
        """Run the hunter domainSearch operation."""
        # Implement the tool logic here
        return f"Running hunter domainSearch operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the hunter domainSearch operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
