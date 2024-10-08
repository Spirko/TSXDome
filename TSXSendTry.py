import socket

verbose = False

# https://github.com/mcgillca/TSX-Polar-Alignment-script/blob/main/PAUI.py
def TSXSendTry(message):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 3040
    BUFFER_SIZE = 1024
    tryMessage = f"""
    /* Java Script */
    try {{
      {message}
    }} catch (e) {{
       out = e;
    }}
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Catch if can't open TCP port.
    try:
        s.connect((TCP_IP, TCP_PORT))
    except:
        queue.put("!"+logtime()+"Could not connect to TSX. Is TSX runnng?")
        queue.put("!"+logtime()+"Have you enabled the TSX TCP server?")
        finish_async_code()
        sys.exit()
        
 
    s.sendall(tryMessage.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()
    if verbose: print(data)
    data2 = data.decode().split("|")
    return data2

def TSXGetDome():
    result = float(TSXSendTry("sky6Dome.GetAzEl(); out=sky6Dome.dAz;")[0])
    return result
