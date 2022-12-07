# Preparando minha máquina

# Alterando arquivo Hosts
sudo vim /etc/hosts

# Adicionando meus domínios ao arquivo
127.0.0.1	blue.labs.com.br
127.0.0.1	green.labs.com.br
127.0.0.1	labs.com.br

# Verificando o ping
➜  ~ ping blue.labs.com.br 
PING blue.labs.com.br (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.032 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.020 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.021 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.016 ms
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.016 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.017 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.021 ms
64 bytes from localhost (127.0.0.1): icmp_seq=8 ttl=64 time=0.016 ms

