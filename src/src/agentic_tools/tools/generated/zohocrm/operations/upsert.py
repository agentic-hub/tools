from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZohocrmUpsertToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoiceId: Optional[str] = Field(None, description="ID of the invoice to delete")
    salesOrderId: Optional[str] = Field(None, description="ID of the sales order to delete")
    Product_Details: Optional[List[Any]] = Field(None, description="Products")
    quoteId: Optional[str] = Field(None, description="ID of the quote to delete")
    vendorId: Optional[str] = Field(None, description="ID of the vendor associated with the purchase order. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    lastName: Optional[str] = Field(None, description="Last Name")
    subject: Optional[str] = Field(None, description="Subject or title of the invoice. If a record with this subject exists it will be updated, otherwise a new one will be created.")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    dealName: Optional[str] = Field(None, description="Name of the deal. If a record with this deal name exists it will be updated, otherwise a new one will be created.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    accountName: Optional[str] = Field(None, description="Name of the account. If a record with this account name exists it will be updated, otherwise a new one will be created.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    Company: Optional[str] = Field(None, description="Company at which the lead works")
    stage: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    dealId: Optional[str] = Field(None, description="ID of the deal to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    purchaseOrderId: Optional[str] = Field(None, description="ID of the purchase order to delete")
    contactId: Optional[str] = Field(None, description="ID of the contact to delete")
    vendorName: Optional[str] = Field(None, description="Name of the vendor. If a record with this vendor name exists it will be updated, otherwise a new one will be created.")
    leadId: Optional[str] = Field(None, description="ID of the lead to delete")
    productName: Optional[str] = Field(None, description="Name of the product. If a record with this product name exists it will be updated, otherwise a new one will be created.")
    productId: Optional[str] = Field(None, description="ID of the product to delete")


class ZohocrmUpsertTool(BaseTool):
    name = "zohocrm_upsert"
    description = "Tool for zohoCrm upsert operation - upsert operation"
    
    def _run(self, **kwargs):
        """Run the zohoCrm upsert operation."""
        # Implement the tool logic here
        return f"Running zohoCrm upsert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zohoCrm upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
