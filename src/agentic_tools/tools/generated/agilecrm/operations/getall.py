from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AgilecrmGetallToolInput(BaseModel):
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter\" target=\"_blank\">Agile CRM guide</a> to creating filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-contacts---companies-api\">here</a>")
    companyId: Optional[str] = Field(None, description="Unique identifier for a particular company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filterJson: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    dealId: Optional[str] = Field(None, description="Unique identifier for a particular deal")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    filterType: Optional[str] = Field(None, description="Filter")
    matchType: Optional[str] = Field(None, description="Must Match")


class AgilecrmGetallTool(BaseTool):
    name = "agilecrm_getall"
    description = "Tool for agileCrm getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the agileCrm getAll operation."""
        # Implement the tool logic here
        return f"Running agileCrm getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the agileCrm getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
