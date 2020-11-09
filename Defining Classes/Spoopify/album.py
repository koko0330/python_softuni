from typing import List
from project.song import Song


class Album:
    name: str
    songs: List[Song]
    published: bool

    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = []

        for song in songs:
            self.add_song(song)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song.name in map(lambda s: s.name, self.songs):
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: Song):
        if self.published:
            return f"Cannot remove songs. Album is published."

        songs_to_be_removed = [s for s in self.songs if s.name == song_name]
        if not songs_to_be_removed:
            return f"Song is not in the album."

        self.songs.remove(songs_to_be_removed[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        album_lines = [
            f"Album {self.name}"
        ]
        song_lines = [
            f'== {s.get_info()}' for s in self.songs

        ]

        return "\n".join(album_lines + song_lines) + "\n"
