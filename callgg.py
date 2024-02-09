#!/usr/bin/env python3

__version__="0.2.2"

def __main__():
    import urllib.request
    from os.path import basename
    from tqdm import tqdm

    def get_file_size(url):
        with urllib.request.urlopen(url) as response:
            size = int(response.headers['Content-Length'])
        return size

    def clone_file(url):
        try:
            file_size = get_file_size(url)
            filename = basename(url)
            with urllib.request.urlopen(url) as response, \
                open(filename, 'wb') as file, \
                tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc=f'Downloading {filename}') as pbar:
                chunk_size = 1024
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    file.write(chunk)
                    pbar.update(len(chunk))
            print(f"\nFile cloned successfully and saved as '{filename}' in the current directory.")
        except Exception as e:
            print(f"Error: {e}")

    import argparse

    parser = argparse.ArgumentParser(description="callgg will execute different functions based on command-line arguments")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="choose a subcommand:")
    subparsers.add_parser('run', help='connect gguf-selector for calling GGUF file(s)')
    clone_parser = subparsers.add_parser('save', help='download a GGUF file from URL; [-h] for details')
    clone_parser.add_argument('url', type=str, help='URL to download from (i.e., callgg save [url])')
    args = parser.parse_args()

    if args.subcommand == 'save':
        clone_file(args.url)
    elif args.subcommand == 'run':
        from gguf_selector import connector
