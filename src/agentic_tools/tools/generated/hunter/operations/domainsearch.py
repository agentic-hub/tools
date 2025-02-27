from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HunterCredentials

class HunterDomainsearchToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    only_emails: Optional[bool] = Field(None, description="Whether to return only the the found emails")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation to consume")
    domain: Optional[str] = Field(None, description="Domain name from which you want to find the email addresses. For example, \"stripe.com\".")


class HunterDomainsearchTool(BaseTool):
    name: str = "hunter_domainsearch"
    connector_id: str = "nodes-base.hunter"
    description: str = "Tool for hunter domainSearch operation - domainSearch operation"
    args_schema: type[BaseModel] | None = HunterDomainsearchToolInput
    credentials: Optional[HunterCredentials] = None
