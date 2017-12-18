#!/usr/bin/python3
import os
import subprocess
import math
import sys

dir_ = 'challenge'
keys = []
weak = set()

if __name__ == '__main__':
    for f in os.listdir(dir_):
        if f.endswith('pem'):
            f = os.path.join(dir_, f)
            p = subprocess.Popen('openssl rsa -in %s -pubin -modulus -noout' % f,
                stdout=subprocess.PIPE, shell=True)
            stdout, stderr = p.communicate()
            cur_key = int(stdout.strip().split(b'=')[1], base=16)
            for key in keys:
                gcd = math.gcd(cur_key, key[0])
                if gcd > 1:
                    weak.add((key[0], gcd, key[1]))
                    weak.add((cur_key, gcd, f))
            keys.append((cur_key, f))

    for w in weak:
        print(w)
