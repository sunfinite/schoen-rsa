```
  root@kali:~/schoen-rsa# openssl version
  OpenSSL 1.1.0f  25 May 2017 (Library: OpenSSL 1.1.0g  2 Nov 2017)
  
  root@kali:~/schoen-rsa# gcc -I/usr/include/openssl/ private-from-pq.c -lcrypto -o get_pk
  private-from-pq.c: In function ‘main’:
  private-from-pq.c:35:3: warning: ‘BN_is_prime’ is deprecated [-Wdeprecated-declarations]
     if (!(BN_is_prime (p, BN_prime_checks, NULL, ctx, NULL)) ||
     ^~
  In file included from /usr/include/openssl/crypto.h:32:0,
                   from /usr/include/openssl/bn.h:33,
                   from private-from-pq.c:2:
  /usr/include/openssl/bn.h:291:1: note: declared here
   DEPRECATEDIN_0_9_8(int
   ^
  private-from-pq.c:36:7: warning: ‘BN_is_prime’ is deprecated [-Wdeprecated-declarations]
         !(BN_is_prime (q, BN_prime_checks, NULL, ctx, NULL))) {
         ^
  In file included from /usr/include/openssl/crypto.h:32:0,
                   from /usr/include/openssl/bn.h:33,
                   from private-from-pq.c:2:
  /usr/include/openssl/bn.h:291:1: note: declared here
   DEPRECATEDIN_0_9_8(int
   ^
  private-from-pq.c:82:3: warning: implicit declaration of function ‘PEM_write_RSAPrivateKey’ [-Wimplicit-function-declaration]
     PEM_write_RSAPrivateKey (stdout, key, NULL, NULL, 0, 0, NULL);
     ^~~~~~~~~~~~~~~~~~~~~~~
  root@kali:~/schoen-rsa# 
```
