from typing import Any
from mcp.server.fastmcp import FastMCP
import aiohttp

# Initialize FastMCP server
mcp = FastMCP("wikidata")

@mcp.tool()
async def run_sparql(query: str) -> dict:
    """Invoke SPARQL query asynchronously on Wikidata.

    Args:
        query: SPARQL query string

    Returns:
        dict: The JSON response from the Wikidata SPARQL endpoint
    """
    # return {"result": "test"}
    # Define the endpoint URL for Wikidata's SPARQL endpoint
    endpoint_url = "https://query.wikidata.org/sparql"
    
    # Set up the query parameters
    params = {
        'query': query,
        'format': 'json'
    }

    # Set up the headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Use aiohttp to send the request asynchronously
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint_url, params=params, headers=headers) as response:
            if response.status == 200:
                return await response.json()  # Return the JSON response
            else:
                print(f"Error: {response.status}")
                return None

if __name__ == "__main__":
    # sparql = """
    # SELECT ?item ?itemLabel WHERE {
    #     ?item wdt:P31 wd:Q5.
    #     SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    # } LIMIT 10
    # """
    # response = asyncio.run(run_sparql(sparql))
    # print(response)

    # Initialize and run the server
    mcp.run(transport='stdio')
