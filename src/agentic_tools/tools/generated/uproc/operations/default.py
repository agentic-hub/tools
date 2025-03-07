from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UprocCredentials

class UprocDefaultToolInput(BaseModel):
    vin: Optional[str] = Field(None, description="The \"Vin\" value to use as a parameter for this Operation")
    price_liter: Optional[str] = Field(None, description="The \"Price liter\" value to use as a parameter for this Operation")
    latitude: Optional[str] = Field(None, description="The \"Latitude\" value to use as a parameter for this Operation")
    format: Optional[str] = Field(None, description="The \"Format\" value to use as a parameter for this Operation")
    count2: Optional[str] = Field(None, description="The \"Count2\" value to use as a parameter for this Operation")
    phone2: Optional[str] = Field(None, description="The \"Phone2\" value to use as a parameter for this Operation")
    mode: Optional[str] = Field(None, description="The \"Mode\" value to use as a parameter for this Operation")
    list: Optional[str] = Field(None, description="The \"List\" value to use as a parameter for this Operation")
    coordinates2: Optional[str] = Field(None, description="The \"Coordinates2\" value to use as a parameter for this Operation")
    included_titles: Optional[str] = Field(None, description="The \"Included titles\" value to use as a parameter for this Operation")
    html: Optional[str] = Field(None, description="The \"Html\" value to use as a parameter for this Operation")
    email: Optional[str] = Field(None, description="The \"Email\" value to use as a parameter for this Operation")
    isocode1: Optional[str] = Field(None, description="The \"Isocode1\" value to use as a parameter for this Operation")
    coordinates1: Optional[str] = Field(None, description="The \"Coordinates1\" value to use as a parameter for this Operation")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    useragent: Optional[str] = Field(None, description="The \"Useragent\" value to use as a parameter for this Operation")
    excluded_titles: Optional[str] = Field(None, description="The \"Excluded titles\" value to use as a parameter for this Operation")
    seniority: Optional[str] = Field(None, description="The \"Seniority\" value to use as a parameter for this Operation")
    replace: Optional[str] = Field(None, description="The \"Replace\" value to use as a parameter for this Operation")
    current_company: Optional[str] = Field(None, description="The \"Current company\" value to use as a parameter for this Operation")
    zipcode2: Optional[str] = Field(None, description="The \"Zipcode2\" value to use as a parameter for this Operation")
    url_dlr: Optional[str] = Field(None, description="The \"Url dlr\" value to use as a parameter for this Operation")
    body: Optional[str] = Field(None, description="The \"Body\" value to use as a parameter for this Operation")
    uuid: Optional[str] = Field(None, description="The \"Uuid\" value to use as a parameter for this Operation")
    length2: Optional[float] = Field(None, description="The \"Length2\" value to use as a parameter for this Operation")
    size: Optional[str] = Field(None, description="The \"Size\" value to use as a parameter for this Operation")
    regex: Optional[str] = Field(None, description="The \"Regex\" value to use as a parameter for this Operation")
    keyword: Optional[str] = Field(None, description="The \"Keyword\" value to use as a parameter for this Operation")
    nif: Optional[str] = Field(None, description="The \"Nif\" value to use as a parameter for this Operation")
    gender: Optional[str] = Field(None, description="The \"Gender\" value to use as a parameter for this Operation")
    source: Optional[str] = Field(None, description="The \"Source\" value to use as a parameter for this Operation")
    province: Optional[str] = Field(None, description="The \"Province\" value to use as a parameter for this Operation")
    width: Optional[str] = Field(None, description="The \"Width\" value to use as a parameter for this Operation")
    ean: Optional[str] = Field(None, description="The \"Ean\" value to use as a parameter for this Operation")
    zipcode1: Optional[str] = Field(None, description="The \"Zipcode1\" value to use as a parameter for this Operation")
    isbn: Optional[str] = Field(None, description="The \"Isbn\" value to use as a parameter for this Operation")
    keywords: Optional[str] = Field(None, description="The \"Keywords\" value to use as a parameter for this Operation")
    location: Optional[str] = Field(None, description="The \"Location\" value to use as a parameter for this Operation")
    category: Optional[str] = Field(None, description="The \"Category\" value to use as a parameter for this Operation")
    number1: Optional[str] = Field(None, description="The \"Number1\" value to use as a parameter for this Operation")
    country: Optional[str] = Field(None, description="The \"Country\" value to use as a parameter for this Operation")
    text: Optional[str] = Field(None, description="The \"Text\" value to use as a parameter for this Operation")
    coin: Optional[str] = Field(None, description="The \"Coin\" value to use as a parameter for this Operation")
    language: Optional[str] = Field(None, description="The \"Language\" value to use as a parameter for this Operation")
    isocode2: Optional[str] = Field(None, description="The \"Isocode2\" value to use as a parameter for this Operation")
    mod: Optional[str] = Field(None, description="The \"Mod\" value to use as a parameter for this Operation")
    imei: Optional[str] = Field(None, description="The \"Imei\" value to use as a parameter for this Operation")
    locality: Optional[str] = Field(None, description="The \"Locality\" value to use as a parameter for this Operation")
    clevel: Optional[str] = Field(None, description="The \"Clevel\" value to use as a parameter for this Operation")
    years1: Optional[float] = Field(None, description="The \"Years1\" value to use as a parameter for this Operation")
    message: Optional[str] = Field(None, description="The \"Message\" value to use as a parameter for this Operation")
    group: Optional[str] = Field(None, description="Resource")
    dni: Optional[str] = Field(None, description="The \"Dni\" value to use as a parameter for this Operation")
    fullpage: Optional[str] = Field(None, description="The \"Fullpage\" value to use as a parameter for this Operation")
    date3: Optional[str] = Field(None, description="The \"Date3\" value to use as a parameter for this Operation")
    duns: Optional[str] = Field(None, description="The \"Duns\" value to use as a parameter for this Operation")
    firstname: Optional[str] = Field(None, description="The \"Firstname\" value to use as a parameter for this Operation")
    number3: Optional[str] = Field(None, description="The \"Number3\" value to use as a parameter for this Operation")
    domain: Optional[str] = Field(None, description="The \"Domain\" value to use as a parameter for this Operation")
    area: Optional[str] = Field(None, description="The \"Area\" value to use as a parameter for this Operation")
    length: Optional[float] = Field(None, description="The \"Length\" value to use as a parameter for this Operation")
    profile: Optional[str] = Field(None, description="The \"Profile\" value to use as a parameter for this Operation")
    current_title: Optional[str] = Field(None, description="The \"Current title\" value to use as a parameter for this Operation")
    message1: Optional[str] = Field(None, description="The \"Message1\" value to use as a parameter for this Operation")
    title: Optional[str] = Field(None, description="The \"Title\" value to use as a parameter for this Operation")
    period: Optional[str] = Field(None, description="The \"Period\" value to use as a parameter for this Operation")
    amount: Optional[str] = Field(None, description="The \"Amount\" value to use as a parameter for this Operation")
    email_to: Optional[str] = Field(None, description="The \"Email to\" value to use as a parameter for this Operation")
    mobile: Optional[str] = Field(None, description="The \"Mobile\" value to use as a parameter for this Operation")
    asin: Optional[str] = Field(None, description="The \"Asin\" value to use as a parameter for this Operation")
    address2: Optional[str] = Field(None, description="The \"Address2\" value to use as a parameter for this Operation")
    bic: Optional[str] = Field(None, description="The \"Bic\" value to use as a parameter for this Operation")
    table: Optional[str] = Field(None, description="The \"Table\" value to use as a parameter for this Operation")
    role: Optional[str] = Field(None, description="The \"Role\" value to use as a parameter for this Operation")
    ip1: Optional[str] = Field(None, description="The \"Ip1\" value to use as a parameter for this Operation")
    coordinates: Optional[str] = Field(None, description="The \"Coordinates\" value to use as a parameter for this Operation")
    find: Optional[str] = Field(None, description="The \"Find\" value to use as a parameter for this Operation")
    address1: Optional[str] = Field(None, description="The \"Address1\" value to use as a parameter for this Operation")
    count1: Optional[str] = Field(None, description="The \"Count1\" value to use as a parameter for this Operation")
    date: Optional[str] = Field(None, description="The \"Date\" value to use as a parameter for this Operation")
    isocode: Optional[str] = Field(None, description="The \"Isocode\" value to use as a parameter for this Operation")
    company: Optional[str] = Field(None, description="The \"Company\" value to use as a parameter for this Operation")
    selector: Optional[str] = Field(None, description="The \"Selector\" value to use as a parameter for this Operation")
    country_code: Optional[str] = Field(None, description="The \"Country code\" value to use as a parameter for this Operation")
    subject: Optional[str] = Field(None, description="The \"Subject\" value to use as a parameter for this Operation")
    number2: Optional[str] = Field(None, description="The \"Number2\" value to use as a parameter for this Operation")
    account: Optional[str] = Field(None, description="The \"Account\" value to use as a parameter for this Operation")
    text2: Optional[str] = Field(None, description="The \"Text2\" value to use as a parameter for this Operation")
    phone: Optional[str] = Field(None, description="The \"Phone\" value to use as a parameter for this Operation")
    password: Optional[str] = Field(None, description="The \"Password\" value to use as a parameter for this Operation")
    phone1: Optional[str] = Field(None, description="The \"Phone1\" value to use as a parameter for this Operation")
    lastname: Optional[str] = Field(None, description="The \"Lastname\" value to use as a parameter for this Operation")
    name: Optional[str] = Field(None, description="The \"Name\" value to use as a parameter for this Operation")
    number: Optional[str] = Field(None, description="The \"Number\" value to use as a parameter for this Operation")
    count: Optional[str] = Field(None, description="The \"Count\" value to use as a parameter for this Operation")
    texts: Optional[str] = Field(None, description="The \"Texts\" value to use as a parameter for this Operation")
    port: Optional[str] = Field(None, description="The \"Port\" value to use as a parameter for this Operation")
    destination: Optional[str] = Field(None, description="The \"Destination\" value to use as a parameter for this Operation")
    text1: Optional[str] = Field(None, description="The \"Text1\" value to use as a parameter for this Operation")
    city: Optional[str] = Field(None, description="The \"City\" value to use as a parameter for this Operation")
    separator: Optional[str] = Field(None, description="The \"Separator\" value to use as a parameter for this Operation")
    fullname: Optional[str] = Field(None, description="The \"Fullname\" value to use as a parameter for this Operation")
    years: Optional[float] = Field(None, description="The \"Years\" value to use as a parameter for this Operation")
    excluded_keywords: Optional[str] = Field(None, description="The \"Excluded keywords\" value to use as a parameter for this Operation")
    iban: Optional[str] = Field(None, description="The \"Iban\" value to use as a parameter for this Operation")
    included_keywords: Optional[str] = Field(None, description="The \"Included keywords\" value to use as a parameter for this Operation")
    ip2: Optional[str] = Field(None, description="The \"Ip2\" value to use as a parameter for this Operation")
    upc: Optional[str] = Field(None, description="The \"Upc\" value to use as a parameter for this Operation")
    rest: Optional[str] = Field(None, description="The \"Rest\" value to use as a parameter for this Operation")
    radius: Optional[str] = Field(None, description="The \"Radius\" value to use as a parameter for this Operation")
    length1: Optional[float] = Field(None, description="The \"Length1\" value to use as a parameter for this Operation")
    field: Optional[str] = Field(None, description="The \"Field\" value to use as a parameter for this Operation")
    distance: Optional[str] = Field(None, description="The \"Distance\" value to use as a parameter for this Operation")
    bcid: Optional[str] = Field(None, description="The \"Bcid\" value to use as a parameter for this Operation")
    glue: Optional[str] = Field(None, description="The \"Glue\" value to use as a parameter for this Operation")
    date1: Optional[str] = Field(None, description="The \"Date1\" value to use as a parameter for this Operation")
    page: Optional[float] = Field(None, description="The \"Page\" value to use as a parameter for this Operation")
    luhn: Optional[str] = Field(None, description="The \"Luhn\" value to use as a parameter for this Operation")
    excluded_companies: Optional[str] = Field(None, description="The \"Excluded companies\" value to use as a parameter for this Operation")
    address: Optional[str] = Field(None, description="The \"Address\" value to use as a parameter for this Operation")
    message2: Optional[str] = Field(None, description="The \"Message2\" value to use as a parameter for this Operation")
    surname: Optional[str] = Field(None, description="The \"Surname\" value to use as a parameter for this Operation")
    fuel_consumption: Optional[str] = Field(None, description="The \"Fuel consumption\" value to use as a parameter for this Operation")
    type: Optional[str] = Field(None, description="The \"Type\" value to use as a parameter for this Operation")
    author: Optional[str] = Field(None, description="The \"Author\" value to use as a parameter for this Operation")
    email_from: Optional[str] = Field(None, description="The \"Email from\" value to use as a parameter for this Operation")
    credit_card: Optional[str] = Field(None, description="The \"Credit card\" value to use as a parameter for this Operation")
    delay: Optional[str] = Field(None, description="The \"Delay\" value to use as a parameter for this Operation")
    date2: Optional[str] = Field(None, description="The \"Date2\" value to use as a parameter for this Operation")
    swift: Optional[str] = Field(None, description="The \"Swift\" value to use as a parameter for this Operation")
    longitude: Optional[str] = Field(None, description="The \"Longitude\" value to use as a parameter for this Operation")
    url: Optional[str] = Field(None, description="The \"Url\" value to use as a parameter for this Operation")
    viewport: Optional[str] = Field(None, description="The \"Viewport\" value to use as a parameter for this Operation")
    nie: Optional[str] = Field(None, description="The \"Nie\" value to use as a parameter for this Operation")
    years2: Optional[float] = Field(None, description="The \"Years2\" value to use as a parameter for this Operation")
    ip: Optional[str] = Field(None, description="The \"Ip\" value to use as a parameter for this Operation")
    isin: Optional[str] = Field(None, description="The \"Isin\" value to use as a parameter for this Operation")
    publisher: Optional[str] = Field(None, description="The \"Publisher\" value to use as a parameter for this Operation")
    cif: Optional[str] = Field(None, description="The \"Cif\" value to use as a parameter for this Operation")
    tin: Optional[str] = Field(None, description="The \"Tin\" value to use as a parameter for this Operation")
    zipcode: Optional[str] = Field(None, description="The \"Zipcode\" value to use as a parameter for this Operation")
    host: Optional[str] = Field(None, description="The \"Host\" value to use as a parameter for this Operation")
    tool: Optional[str] = Field(None, description="The Operation to consume")
    taxid: Optional[str] = Field(None, description="The \"Taxid\" value to use as a parameter for this Operation")
    included_companies: Optional[str] = Field(None, description="The \"Included companies\" value to use as a parameter for this Operation")


class UprocDefaultTool(BaseTool):
    name: str = "uproc_default"
    connector_id: str = "nodes-base.uproc"
    description: str = "Tool for uproc default operation - default operation"
    args_schema: type[BaseModel] | None = UprocDefaultToolInput
    credentials: Optional[UprocCredentials] = None
