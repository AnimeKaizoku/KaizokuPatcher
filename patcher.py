import os, sys
from subprocess import check_output, Popen, PIPE, STDOUT

def path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

patchfiles = [x for x in os.listdir() if x.endswith('.patch')]

if len(patchfiles) == 0:
    print('No patches found. Press any key to exit.')
    os.system('pause >NUL')
    sys.exit()

for patchfile in patchfiles:
    infile = patchfile.replace('.patch', '.mkv')
    info = str(check_output(path(f'xdelta3 printhdr "{patchfile}"')))
    outfile = info.split('(output):')[1].split('.mkv')[0].strip().split('\\\\')[-1]+'.mkv'
    print(f'\nPatching "{infile}" to "{outfile}"')
    cmd = f'xdelta3.exe -d -s "{infile}" "{patchfile}" "{outfile}"'
    p = Popen(path(cmd), stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True)
    output = str(p.stdout.read())
    if 'overwrite output file' in output:
        print('The output filename already exists. Delete it and try again.')
    elif 'file open failed' in output:
        print('Make sure the video and the patch file have the same name.')
    elif 'target window checksum mismatch' in output:
        print('This patch is not made for this file.')
    elif len(output) == 3:
        print('Done!')
    else:
        print((output))

print('Visit AnimeKaizoku.com for more!\nPress any key to exit.')
os.system('pause >NUL')