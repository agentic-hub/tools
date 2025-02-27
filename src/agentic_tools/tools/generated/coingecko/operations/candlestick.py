from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoCandlestickToolInput(BaseModel):
    base_currency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    days: Optional[str] = Field(None, description="Return data for this many days in the past from now")
    resource: Optional[str] = Field(None, description="Resource")
    base_currencies: Optional[str] = Field(None, description="baseCurrencies")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    quote_currencies: Optional[str] = Field(None, description="quoteCurrencies")
    quote_currency: Optional[str] = Field(None, description="The second currency in the pair. For BTC:ETH this is ETH. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coin_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoCandlestickTool(BaseTool):
    name: str = "coingecko_candlestick"
    connector_id: str = "nodes-base.coinGecko"
    description: str = "Tool for coinGecko candlestick operation - candlestick operation"
    args_schema: type[BaseModel] | None = CoingeckoCandlestickToolInput
