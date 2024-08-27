import requests
from requests.auth import HTTPBasicAuth


def get_spotify_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    payload = {'grant_type': 'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url,
                             data=payload,
                             headers=headers,
                             auth=HTTPBasicAuth(client_id, client_secret))

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return {
            "error": "Failed to get token",
            "status_code": response.status_code,
            "message": response.text
        }


def get_spotify_track_info(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    """    try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            print("Success!")
            return response.json()
    """
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the track info as a JSON object
    else:
        return {
            "error": "Failed to get track info",
            "status_code": response.status_code,
            "message": response.text
        }
def get_artist_id(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        artists = response.json().get('artists', {}).get('items', [])
        if artists:
            print("dshjhs")
            print(artists[0]['id'])
            return artists[0]['id'] 
        else:
            return None
    else:
        return None
def get_artist_albums(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "include_groups": "album,single",  
        "limit": 5 
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return []
def get_album_tracks(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return []

def get_all_songs_by_artist(token, artist_name):
    artist_id = get_artist_id(token, artist_name)
    print("sdsdsdsgfgf")
    print(artist_id)
    if artist_id is None:
        return {"error": "Artist not found"}

    albums = get_artist_albums(token, artist_id)

    all_tracks = []

    for album in albums:
        print(album)
        """
        album_id = album['id']
        tracks = get_album_tracks(token, album_id)

        for track in tracks:
            track_info = {
                "track_name": track['name'],
                "album_name": album['name'],
                "artist_name": artist_name,
                "track_id": track['id'],
                "track_url": track['external_urls']['spotify']
            }
            all_tracks.append(track_info)
        """
        
    return all_tracks
client_id = 'b53917d5c1be4ff7a21152d65a71d5a8'
client_secret = 'f6a465ee28cd40c4824ea3dda514dec2'
token_info = get_spotify_token(client_id, client_secret)
print(f" API Key for this session: {token_info}")
"""
track_id = "4E1SihVWKU6rcJvxnxakSd?si=4e27896b09274dc4"

track_info = get_spotify_track_info(token_info, track_id)
print(track_info)
artist_name = track_info['artists'][0]['name']

href = track_info['artists'][0]['href']

print(f"Artist Name: {artist_name}")
print(f"Href: {href}")

artist_name = "V"
"""
"""
songs = get_all_songs_by_artist(token_info, artist_name)
for song in songs:
    print(f"Track: {song['track_name']}, Album: {song['album_name']}, Artist: {song['artist_name']}, URL: {song['track_url']}")
    """
#4pADjHPWyrlAF0FA7joK2H--Jay Sean
#3JsHnjpbhX4SnySpvpa9DK--V

url = "https://api.spotify.com/v1/artists/3JsHnjpbhX4SnySpvpa9DK,4pADjHPWyrlAF0FA7joK2H/albums"
headers = {
    "Authorization": f"Bearer {token_info}"
}
params = {
    "include_groups": "album,single",  
    "limit": 5 
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    albums=response.json().get('items', [])
    #print(albums)
    for album in albums:
        album_id = album['id']
        tracks = get_album_tracks(token_info, album_id)

        for track in tracks:
                print(track['name'])
                print(album['name'])
                