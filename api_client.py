import aiohttp
from config import API_BASE_URL, headers

async def fetch_data(session, url, params=None):
    async with session.get(url, params=params, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            text = await response.text()
            raise aiohttp.ClientResponseError(
                response.request_info,
                response.history,
                status=response.status,
                message=text[:200],
                headers=response.headers,
            )

async def search_players(session, name, year):
    url = f"{API_BASE_URL}/player/search"
    params = {"searchTerm": name, "year": year}
    return await fetch_data(session, url, params)

async def get_player_stats(session, player_id, year):
    url = f"{API_BASE_URL}/stats/player/season"
    params = {"year": year, "playerId": player_id}
    return await fetch_data(session, url, params)