#!/usr/bin/python
# Made with <3 by Fran González (@spaceisstrange)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a
#  copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

class ResultItem(object):
    """
    Defines a general result item
    """
    def __init__(self, json):
        """
        Initializes the ResultItem class from the JSON provided
        :param json: String. Raw JSON data to fetch information from
        """
        self.artist_name = json['artistName']
        self.type = None

        if 'wrapperType' in json:
            self.type = json['wrapperType']

            if 'collectionType' in json:
                self.collection_type = json['collectionType']
            elif 'artistType' in json:
                self.artist_type = json['artistType']
            elif 'kind' in json:
                self.track_type = json['kind']
        elif 'kind' in json:
            self.type = json['kind']

        if 'primaryGenreName' in json:
            self.primary_genre_name = json['primaryGenreName']

        if 'trackName' in json:
            self.track_name = json['trackName']

        if 'trackCensoredName' in json:
            self.track_censored_name = json['trackCensoredName']

        if 'trackViewUrl' in json:
            self.track_view_url = json['trackViewUrl']

        if 'previewUrl' in json:
            self.preview_url = json['previewUrl']

        if 'artworkUrl30' in json:
            self.artwork_url_30 = json['artworkUrl30']

        if 'artworkUrl60' in json:
            self.artwork_url_60 = json['artworkUrl60']

        if 'artworkUrl100' in json:
            self.artwork_url_100 = json['artworkUrl100']

        if 'artworkUrl512' in json:
            self.artwork_url_512 = json['artworkUrl512']

        if 'collectionName' in json:
            self.collection_name = json['collectionName']

        if 'trackPrice' in json:
            self.track_price = json['trackPrice']

        if 'releaseDate' in json:
            self.release_date = json['releaseDate']

        if 'trackExplicitness' in json:
            self.track_explicitness = json['trackExplicitness']

        if 'trackTimeMillis' in json:
            self.track_time = json['trackTimeMillis']

        if 'country' in json:
            self.country = json['country']

        if 'currency' in json:
            self.currency = json['currency']

        if 'copyright' in json:
            self.copyright = json['copyright']

        if 'price' in json:
            self.price = json['price']

    def __repr__(self):
        """
        Retrieves all keys in the class as a String
        :return: String. All the keys available in the class
        """
        string = ''

        for key, value in self.__dict__.items():
            if not key.startswith('__'):
                string += '\n' + key + ':' + str(value)

        return string
