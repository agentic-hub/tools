from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZohocrmCredentials

class ZohocrmUpsertToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoice_id: Optional[str] = Field(None, description="ID of the invoice to delete")
    sales_order_id: Optional[str] = Field(None, description="ID of the sales order to delete")
    product__details: Optional[List[Any]] = Field(None, description="Products")
    quote_id: Optional[str] = Field(None, description="ID of the quote to delete")
    vendor_id: Optional[str] = Field(None, description="ID of the vendor associated with the purchase order. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    subject: Optional[str] = Field(None, description="Subject or title of the invoice. If a record with this subject exists it will be updated, otherwise a new one will be created.")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    deal_name: Optional[str] = Field(None, description="Name of the deal. If a record with this deal name exists it will be updated, otherwise a new one will be created.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    account_name: Optional[str] = Field(None, description="Name of the account. If a record with this account name exists it will be updated, otherwise a new one will be created.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    company: Optional[str] = Field(None, description="Company at which the lead works")
    stage: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    deal_id: Optional[str] = Field(None, description="ID of the deal to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    purchase_order_id: Optional[str] = Field(None, description="ID of the purchase order to delete")
    contact_id: Optional[str] = Field(None, description="ID of the contact to delete")
    vendor_name: Optional[str] = Field(None, description="Name of the vendor. If a record with this vendor name exists it will be updated, otherwise a new one will be created.")
    lead_id: Optional[str] = Field(None, description="ID of the lead to delete")
    product_name: Optional[str] = Field(None, description="Name of the product. If a record with this product name exists it will be updated, otherwise a new one will be created.")
    product_id: Optional[str] = Field(None, description="ID of the product to delete")


class ZohocrmUpsertTool(BaseTool):
    name: str = "zohocrm_upsert"
    description: str = "Tool for zohoCrm upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = ZohocrmUpsertToolInput
    credentials: Optional[ZohocrmCredentials] = None
