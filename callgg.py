#!/usr/bin/env python3

__version__="1.0.3"

def __main__():
    import urllib.request
    from os.path import basename
    from llama_core.rich.progress import Progress # generic module adopted (lama_core >=0.1.2 required)

    def get_file_size(url):
        with urllib.request.urlopen(url) as response:
            size = int(response.headers['Content-Length'])
        return size

    def format_size(size_bytes):
        return f"{size_bytes / (1024 * 1024):.2f} MB"

    def clone_file(url): # no more invalid certificate issues (llama_core >=0.1.9 required)
        try:
            file_size = get_file_size(url)
            filename = basename(url)
            with Progress(transient=True) as progress:
                task = progress.add_task(f"Downloading {filename}", total=file_size)
                with urllib.request.urlopen(url) as response, open(filename, 'wb') as file:
                    chunk_size = 1024
                    downloaded = 0
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        file.write(chunk)
                        downloaded += len(chunk)
                        progress.update(task, completed=downloaded, description=f"Downloading {filename} [green][{format_size(downloaded)} / {format_size(file_size)}]")
            print(f"File cloned successfully and saved as '{filename}'({format_size(file_size)}) in the current directory.")
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
