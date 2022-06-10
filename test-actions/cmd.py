import shlex
import subprocess
import json
import sys
import os

def get_uid():
    try:
        with open('/proc/1/environ') as f:
            e = f.read()
        uid = [x for x in e.split('\x00') if 'POD_UID' in x]
        uid = uid[0].split('=')[1]
        return uid
    except Exception as e:
        print(e)
        return 'unknown'

def log_action_pod(params):
    o = {'params': params, 'pod-uid': get_uid(), 'action': os.environ.get('__OW_ACTION_NAME', 'unknown')}
    print(f'Logging action-pod info {json.dumps(o)}')
    with open('/var/log/f3/action-pods', 'a') as f:
        json.dump(o, f)
        f.write('\n')

def main(dict):
    log_action_pod(dict)

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
    #log_action_pod(sys.argv[1])
    print(main(json.loads(sys.argv[1])))
