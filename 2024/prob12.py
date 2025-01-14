sock = input()
sock_dict = {}
while sock != "END END END":
    if sock_dict.get(sock):
        sock_dict[sock] += 1
    else:
        sock_dict[sock] = 1
    sock = input()

missing = False
for sock in sock_dict.keys():
    if sock_dict.get(sock) % 2 == 1:
        print(sock)
        missing = True

if not missing:
    print("No missing socks")
    