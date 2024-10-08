
import serial

resolution = 18911117 / 360

def MDriveSend(command, port="COM5", baudrate=19200):
    
    with serial.Serial(
                port,
                baudrate,
                timeout=2,
                write_timeout=2) as ser:
        data = f'\n{command}\n'
        ser.write(data.encode())
        result = ser.read(1000)
        return result.decode()  

def MDriveAzGet():
    result = MDriveSend('APR P')
    cur_pos = int(result.split('\n')[2])
    return cur_pos / resolution

def ClosestAz(az, cur_az):
    delta = (az - cur_az)
    close_delta = (delta + 180)%360 - 180
    return cur_az + close_delta

def MDriveAzGoto(az):
    cur_az = MDriveAzGet()

    new_az = ClosestAz(az, cur_az)
    new_pos = int(new_az * resolution)

    result = MDriveSend(f'AMA {new_pos}')
    return result


if __name__ == '__main__':
    pass
