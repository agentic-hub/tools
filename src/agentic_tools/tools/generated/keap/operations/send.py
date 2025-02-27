from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KeapCredentials

class KeapSendToolInput(BaseModel):
    contact_ids: Optional[str] = Field(None, description="Contact IDs to receive the email. Multiple can be added seperated by comma.")
    tag_ids: Optional[str] = Field(None, description="tagIds")
    user_id: Optional[str] = Field(None, description="The infusionsoft user to send the email on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addresses_ui: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subject: Optional[str] = Field(None, description="The subject line of the email")
    operation: Optional[str] = Field(None, description="Operation")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    order_id: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Attachments to be sent with each copy of the email, maximum of 10 with size of 1MB each")
    faxes_ui: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    product_id: Optional[str] = Field(None, description="Product ID")


class KeapSendTool(BaseTool):
    name: str = "keap_send"
    description: str = "Tool for keap send operation - send operation"
    args_schema: type[BaseModel] | None = KeapSendToolInput
    credentials: Optional[KeapCredentials] = None
