from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoPriceToolInput(BaseModel):
    base_currency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    search_by: Optional[str] = Field(None, description="Search by coin ID or contract address")
    contract_addresses: Optional[str] = Field(None, description="The contract address of tokens, comma-separated")
    base_currencies: Optional[str] = Field(None, description="baseCurrencies")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    platform_id: Optional[str] = Field(None, description="The ID of the platform issuing tokens")
    quote_currencies: Optional[str] = Field(None, description="quoteCurrencies")
    coin_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoPriceTool(BaseTool):
    name: str = "coingecko_price"
    connector_id: str = "nodes-base.coinGecko"
    description: str = "Tool for coinGecko price operation - price operation"
    args_schema: type[BaseModel] | None = CoingeckoPriceToolInput
