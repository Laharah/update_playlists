#!/usr/bin/env python3
"""Copy m3u(8) playlists and update the track paths."""
import re
from pathlib import Path, PurePath, PureWindowsPath


def main(playlist_dir, output_dir, replace=None, overwrite=False, update_only=False):
    if replace:
        old_m_dir, new_m_dir = replace
        if '\\' in str(old_m_dir) or re.match(r'\w:', str(old_m_dir)):
            old_m_dir = PureWindowsPath(old_m_dir)
    for playlist in playlist_dir.rglob('*.m3u*'):
        dest = playlist.relative_to(playlist_dir)
        dest = output_dir / dest
        if not (overwrite or update_only) and dest.exists():
            print(f'{dest} already exists, skipping.')
            continue
        if (update_only and dest.exists()
                and dest.stat().st_mtime > playlist.stat().st_mtime):
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(playlist) as fin, open(dest, 'wb') as fout:
            for track in fin:
                track = track.strip()
                if re.match(r'\w:', track):
                    track = PureWindowsPath(track)
                else:
                    track = Path(track)
                if replace:
                    track = new_m_dir / track.relative_to(old_m_dir)
                fout.write(bytes(str(track), 'utf8'))
                fout.write(b'\n')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('update_playlists', description=__doc__)
    parser.add_argument('playlist_dir', type=Path, help='Path to read m3u files from.')
    parser.add_argument('output_dir', type=Path, help='Path to write m3u files to.')
    parser.add_argument('-m',
                        '--replace_music_dir',
                        dest='replace',
                        nargs=2,
                        type=PurePath,
                        help='Replace OLDMUSICDIR with LOCALMUSICDIR on each track.',
                        metavar=('OLDMUSICDIR', 'LOCALMUSICDIR'))
    overwrites = parser.add_mutually_exclusive_group()
    overwrites.add_argument('-f',
                            '--overwrite',
                            dest='overwrite',
                            action='store_true',
                            help='Overwrite exsisting playlists.')
    overwrites.add_argument('-u',
                            '--update_only',
                            dest='update_only',
                            action='store_true',
                            help='Overwrite only if source is newer than destination.')
    options = parser.parse_args()
    main(**vars(options))
