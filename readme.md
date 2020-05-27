# Update Playlists

Simple script to update m3u playlists for local playback

## Requrements
* Python 3.7+

## Installation

Place `update_playlists.py` in your path and make it executable.

For example:
```
$> cp update_playlists.py /usr/local/bin/update_playlists
$> chmod +x /usr/local/bin/update_playlists
```

## Usage
```
usage: update_playlists [-h] [-m OLDMUSICDIR LOCALMUSICDIR] [-f | -u]
                        playlist_dir output_dir

Copy m3u(8) playlists and update the track paths.

positional arguments:
  playlist_dir          Path to read m3u files from.
  output_dir            Path to write m3u files to.

optional arguments:
  -h, --help            show this help message and exit
  -m OLDMUSICDIR LOCALMUSICDIR, --replace_music_dir OLDMUSICDIR LOCALMUSICDIR
                        Replace OLDMUSICDIR with LOCALMUSICDIR on each track.
  -f, --overwrite       Overwrite exsisting playlists.
  -u, --update_only     Overwrite only if source is newer than destination.
```
