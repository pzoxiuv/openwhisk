import shlex
import subprocess
import json
import sys
import os

def main(dict):
    if 'command' in dict:
        cmd = dict['command']
    else:
        print('heeeey')
        return

    print(f'Running {cmd}')
    #print(f'ENV: {os.environ}')
    #proc = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(f'Done, got stdout: {proc.stdout}\nstderr: {proc.stderr}\n')
    return {'stdout': proc.stdout.decode('ascii'), 'stderr': proc.stderr.decode('ascii')}

if __name__ == '__main__':
    print(main(json.loads(sys.argv[1])))
