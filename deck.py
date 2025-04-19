import asyncio

from homedeck.homedeck import HomeDeck


async def main():
    deck = HomeDeck()
    await deck.connect()

asyncio.run(main())
