from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AgilecrmDeleteToolInput(BaseModel):
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    jsonNotice: Optional[str] = Field(None, description="See <a href=\"https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter\" target=\"_blank\">Agile CRM guide</a> to creating filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-contacts---companies-api\">here</a>")
    companyId: Optional[str] = Field(None, description="ID of company to delete")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filterJson: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    dealId: Optional[str] = Field(None, description="ID of deal to delete")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="ID of contact to delete")
    filterType: Optional[str] = Field(None, description="Filter")
    matchType: Optional[str] = Field(None, description="Must Match")


class AgilecrmDeleteTool(BaseTool):
    name = "agilecrm_delete"
    description = "Tool for agileCrm delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the agileCrm delete operation."""
        # Implement the tool logic here
        return f"Running agileCrm delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the agileCrm delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
