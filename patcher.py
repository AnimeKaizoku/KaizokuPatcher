import os, sys
from subprocess import check_output, Popen, PIPE, STDOUT

def path(relative):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

patches = [x for x in os.listdir() if x.endswith('.patch')]

if len(patches) == 0:
    print('No patches found. Press any key to exit.')
    os.system('pause >NUL')
    sys.exit()

for patch in patches:
    infile = patch.replace('.patch', '.mkv')
    info = str(check_output(path(f'xdelta3 printhdr "{patch}"')))
    outfile = info.split('(output):')[1].split('.mkv')[0].strip().split('\\\\')[-1]+'.mkv'

    print(f'Patching "{infile}" to "{outfile}"', end='')
    if not os.path.exists('Patched'):
        os.mkdir('Patched')

    cmd = f'xdelta3.exe -d -s "{infile}" "{patch}" "Patched\\{outfile}"'
    p = Popen(path(cmd), stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True)
    output = str(p.stdout.read())

    if 'overwrite output file' in output:
        print('\nThe output filename already exists. Delete it and try again.')
    elif 'file open failed' in output:
        print('\nMake sure the encode and the patch files have the same name.')
    elif 'target window checksum mismatch' in output:
        print('\nThis patch is not made for this encode.')
    elif len(output) == 3:
        print(' - Done!')
    else:
        print((output))

print('\nVisit AnimeKaizoku.com for more!\nPress any key to exit.')
os.system('pause >NUL')