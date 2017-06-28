import requests
import os

# URL Only returns a single URI
# If need to search multiple songs, need to remove the '/' at the end of the URL
# Remember to source secrets.sh for API key.

VERSION = '0.1'
URL = 'http://api.guitarparty.com/v2/%(resource)s/'
QUERY = 'http://api.guitarparty.com/v2/%(resource)s'
API_KEY = os.environ['GUITAR_PARTY_API_KEY']

def request(resource, **params):
    """Returns JSON from a single URI (songs, artists, or chords)."""
    options = {
        'headers': {
            'Guitarparty-Api-Key': API_KEY,
        },
    }
    options.update(params)
    r = requests.get(URL % {'resource': resource}, **options)
    return r.json()


def query(resource, **params):
    """Returns JSON objects from a query."""
    options = {
        'headers': {
            'Guitarparty-Api-Key': API_KEY,
        },
    }
    options.update(params)
    r = requests.get(QUERY % {'resource': resource}, **options)
    return r.json()


def format_search(search_term):
    """Replace any spaces with '+'."""

    search_term = search_term.strip()
    search_split = search_term.split(' ')
    return '+'.join(search_split)


def query_songs(search_term):
    """Get JSON objects of songs. Search term must have '+' instead of spaces."""

    return query('songs/?query={}'.format(format_search(search_term)))


def extract_songs():

    pass


over_the_rainbow = request('songs/365')
chords_dict = over_the_rainbow['chords']
chord_names = []

for chord in chords_dict:
    chord_names.append(chord['name'])