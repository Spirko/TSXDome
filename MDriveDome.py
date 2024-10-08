
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

def close_delta(az, cur_az):
    delta = (az - cur_az)
    return (delta + 180)%360 - 180

def close_azimuth(az, cur_az):
    cur_delta = close_delta(az, cur_az)
    return cur_az + cur_delta

def MDriveAzGoto(az):
    cur_az = MDriveAzGet()
        
    if abs(close_delta(az,cur_az)) > 2:
      new_az = close_azimuth(az, cur_az)
      new_pos = int(new_az * resolution)
      result = MDriveSend(f'AMA {new_pos}')
    else:

      print(f"Slew from {cur_az} to {az} rotation not needed for delta {abs(close_delta(az,cur_az))}")
      result = None
    return result


if __name__ == '__main__':
    pass
