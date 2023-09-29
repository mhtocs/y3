import asyncio
import json
from shazamio import Shazam, Serialize


async def main():
    shazam = Shazam()
    out = await shazam.recognize_song('test.mp3')
    if (out is not None):
        track = out['track']
        title = track['title']
        artist = await shazam.artist_about(track['artists'][0]['adamid'])
        print(f"{json.dumps(track, indent=4)}")
        print(f"Song {title} by {artist['data'][0]['attributes']['name']}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
