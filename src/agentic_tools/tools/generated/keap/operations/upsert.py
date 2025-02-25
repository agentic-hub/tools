from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KeapUpsertToolInput(BaseModel):
    duplicateOption: Optional[str] = Field(None, description="Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated.")
    emailsUi: Optional[Dict[str, Any]] = Field(None, description="Emails")
    tagIds: Optional[str] = Field(None, description="tagIds")
    userId: Optional[str] = Field(None, description="The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addressesUi: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    phonesUi: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    socialAccountsUi: Optional[Dict[str, Any]] = Field(None, description="Social Accounts")
    orderId: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[str] = Field(None, description="Contact ID")
    noteId: Optional[str] = Field(None, description="Note ID")
    faxesUi: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    productId: Optional[str] = Field(None, description="Product ID")


class KeapUpsertTool(BaseTool):
    name = "keap_upsert"
    description = "Tool for keap upsert operation - upsert operation"
    
    def _run(self, **kwargs):
        """Run the keap upsert operation."""
        # Implement the tool logic here
        return f"Running keap upsert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the keap upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
