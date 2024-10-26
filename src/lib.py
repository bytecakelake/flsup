from pkg import *

def listup(prefix: PATH, extension: str):
    return prefix.rglob('*.' + extension)

def parseargs() -> dict:

    EXPRESSION = r'\s*-(\w+)=(\S*)'
    arg_pattern = RE.compile(EXPRESSION)
    args = {}
    ii = " \n".join(sys.argv[1:])
    i = arg_pattern.finditer(ii)
    for v in i:
        args[v.group(1)] = v.group(2)
    if 'help' in args:
        sys.stdout.write('Usage: python3 filelistup -prefix={start scan files of path} -extension={file extension}\n')
        sys.exit(0)
    
    if 'prefix' not in args:
        sys.stderr.write('NOTE: prefix not found. Use -help=all to see usage\n')
        sys.exit(1)
    if 'extension' not in args:
        sys.stderr.write('NOTE: extension not found. Use -help=all to see usage\n')
        sys.exit(1)
    return args


__all__ = ['parseargs', 'listup']