import socket 
from time import sleep

ip  = input("Digite o host ou ip a ser verificado: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count += 1

print()
print('='*50)
print("\nComeçando checagem...\n")
sleep(3)

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)

    code = client.connect_ex((ip, port))


    if code == 0:
        print(f"{port}  -> Porta aberta")
    else:
        print(f"{port}  -> Porta fechada")
    
print("\nScan finalizado")