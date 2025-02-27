from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KeapCredentials

class KeapUpsertToolInput(BaseModel):
    duplicate_option: Optional[str] = Field(None, description="Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated.")
    emails_ui: Optional[Dict[str, Any]] = Field(None, description="Emails")
    tag_ids: Optional[str] = Field(None, description="tagIds")
    user_id: Optional[str] = Field(None, description="The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addresses_ui: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    social_accounts_ui: Optional[Dict[str, Any]] = Field(None, description="Social Accounts")
    order_id: Optional[str] = Field(None, description="Order ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")
    faxes_ui: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    product_id: Optional[str] = Field(None, description="Product ID")


class KeapUpsertTool(BaseTool):
    name: str = "keap_upsert"
    description: str = "Tool for keap upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = KeapUpsertToolInput
    credentials: Optional[KeapCredentials] = None
