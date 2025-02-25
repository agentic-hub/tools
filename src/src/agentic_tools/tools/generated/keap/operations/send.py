from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class KeapSendToolInput(BaseModel):
    contactIds: Optional[str] = Field(None, description="Contact IDs to receive the email. Multiple can be added seperated by comma.")
    tagIds: Optional[str] = Field(None, description="tagIds")
    userId: Optional[str] = Field(None, description="The infusionsoft user to send the email on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addressesUi: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subject: Optional[str] = Field(None, description="The subject line of the email")
    operation: Optional[str] = Field(None, description="Operation")
    phonesUi: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    orderId: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contactId: Optional[str] = Field(None, description="Contact ID")
    noteId: Optional[str] = Field(None, description="Note ID")
    attachmentsUi: Optional[Dict[str, Any]] = Field(None, description="Attachments to be sent with each copy of the email, maximum of 10 with size of 1MB each")
    faxesUi: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    productId: Optional[str] = Field(None, description="Product ID")


class KeapSendTool(BaseTool):
    name = "keap_send"
    description = "Tool for keap send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the keap send operation."""
        # Implement the tool logic here
        return f"Running keap send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the keap send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
