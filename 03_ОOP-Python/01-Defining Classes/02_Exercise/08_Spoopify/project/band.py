from typing import List
from project.album import Album


class Band:
    name: str
    albums: List[Album]

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album.name in map(lambda a: a.name, self.albums):
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        list_of_albums = [album.name for album in self.albums]
        if album_name not in list_of_albums:
            return f"Album {album_name} is not found."

        album = self.albums[list_of_albums.index(album_name)]
        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        return "\n".join([
            f"Band {self.name}"
        ] + [
            a.details() for a in self.albums
        ]) + "\n"
