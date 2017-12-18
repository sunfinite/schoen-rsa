#!/usr/bin/python3
import os
import subprocess
import math
import sys
import ast

lines = open(sys.argv[1]).read().strip().split('\n')
weak = []
for l in lines:
    weak.append(ast.literal_eval(l))
dir_ = 'challenge'

if __name__ == '__main__': 
    r = []
    for w in weak:
        p = subprocess.Popen("./get_pk %d %d" % (w[1], w[0] // w[1]), 
            shell=True, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        with open('key.pem', 'wb') as fout:
            fout.write(stdout.split(b'\n\n')[1])
        f = w[2].split('.')[0]
        i = int(f.split('/')[1])
        f += '.bin'
        print("Decrypting %s" % f)
        cmd = 'openssl rsautl -decrypt -in %s -inkey key.pem' % f
        p = subprocess.Popen(cmd, 
            shell=True, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Decrypted text: ", stdout)
        r.append((i, stdout))

    print("\n\nFinal text in order:\n")
    print(''.join(x[1].decode('utf-8') for x in sorted(r, key=lambda x: x[0])))
