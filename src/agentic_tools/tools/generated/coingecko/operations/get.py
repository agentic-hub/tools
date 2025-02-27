from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoGetToolInput(BaseModel):
    base_currency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    contract_address: Optional[str] = Field(None, description="Token's contract address")
    search_by: Optional[str] = Field(None, description="Search by coin ID or contract address")
    base_currencies: Optional[str] = Field(None, description="baseCurrencies")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    platform_id: Optional[str] = Field(None, description="The ID of the platform issuing tokens")
    quote_currencies: Optional[str] = Field(None, description="quoteCurrencies")
    coin_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoGetTool(BaseTool):
    name: str = "coingecko_get"
    description: str = "Tool for coinGecko get operation - get operation"
    args_schema: type[BaseModel] | None = CoingeckoGetToolInput
