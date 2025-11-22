import httpx
from pydantic import Field
from typing import Annotated, Literal, List
from fastmcp import FastMCP
from .tokenmanager import ChemspaceTokenManager

# function input types
Country = Annotated[
    str,
    Field(
        description="The country you want your order to be shipped to as two-letter country ISO code, e.g DE, US, FR"
    ),
]

ResultCount = Annotated[
    int, Field(description="Maximum number of results on a page", ge=1)
]

ResultPage = Annotated[int, Field(description="Number of the page", ge=1)]

ProductCategory = Literal["CSSB", "CSSS", "CSMB", "CSMS", "CSCS"]

ProductCategories = Annotated[
    List[ProductCategory],
    Field(
        description=(
            "A list of product categories to search"
            "CSSB - In-stock building blocks"
            "CSSS - In-stock screening compounds"
            "CSMB - Make-on-demand building blocks"
            "CSMS - Make-on-demand screening compounds"
            "CSCS - Custom request"
        ),
        min_length=1,
    ),
]


def register_tools(mcp: FastMCP, mgr: ChemspaceTokenManager):
    @mcp.tool(enabled=True)
    async def search_exact(
        smiles: str,
        shipToCountry: Country = "US",
        count: ResultCount = 10,
        page: ResultPage = 1,
        categories: ProductCategories = ["CSSB", "CSMB"],
    ):
        """Exact search by SMILES"""
        access_token = await mgr.get_token()

        async with httpx.AsyncClient() as client:
            r = await client.post(
                url="https://api.chem-space.com/v4/search/exact",
                headers={
                    "Accept": "application/json; version=4.1",
                    "Authorization": f"Bearer {access_token}",
                },
                params={
                    "shipToCountry": shipToCountry,
                    "count": count,
                    "page": page,
                    "categories": ",".join(categories),
                },
                files={
                    "SMILES": (None, smiles),
                },
            )
        r.raise_for_status()
        data = r.json()

        return data

    @mcp.tool(enabled=True)
    async def search_substructure(
        smiles: str,
        shipToCountry: Country = "US",
        count: ResultCount = 10,
        page: ResultPage = 1,
        categories: ProductCategories = ["CSSB", "CSMB"],
    ):
        """Substructure search by SMILES"""

        access_token = await mgr.get_token()

        async with httpx.AsyncClient() as client:
            r = await client.post(
                url="https://api.chem-space.com/v4/search/sub",
                headers={
                    "Accept": "application/json; version=4.1",
                    "Authorization": f"Bearer {access_token}",
                },
                params={
                    "shipToCountry": shipToCountry,
                    "count": count,
                    "page": page,
                    "categories": ",".join(categories),
                },
                files={
                    "SMILES": (None, smiles),
                },
            )
        r.raise_for_status()
        data = r.json()

        return data

    @mcp.tool(enabled=True)
    async def search_similarity(
        smiles: str,
        shipToCountry: Country = "US",
        count: ResultCount = 10,
        page: ResultPage = 1,
        categories: ProductCategories = ["CSSB", "CSMB"],
    ):
        """Similarity search by SMILES"""
        access_token = await mgr.get_token()

        async with httpx.AsyncClient() as client:
            r = await client.post(
                url="https://api.chem-space.com/v4/search/sub",
                headers={
                    "Accept": "application/json; version=4.1",
                    "Authorization": f"Bearer {access_token}",
                },
                params={
                    "shipToCountry": shipToCountry,
                    "count": count,
                    "page": page,
                    "categories": ",".join(categories),
                },
                files={
                    "SMILES": (None, smiles),
                },
            )
        r.raise_for_status()
        data = r.json()

        return data
