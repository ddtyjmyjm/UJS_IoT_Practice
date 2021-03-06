import time

import serial


class USBInterface(object):
    # usb object
    def __init__(self):
        
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 9600,timeout=3)
            time.sleep(3)
            print('A Serial Echo Is Running...')
        except Exception as e:
            print('open serial 0 failed.')
            try:
                self.ser = serial.Serial('/dev/ttyACM1', 9600)
                print('A Serial Echo Is Running...')
            except Exception as e:
                print('open serial 1 failed.')
        """ winodws
        try:
            self.ser = serial.Serial('COM4', 9600, timeout=3)
            print('A Serial Echo Is Running...')
            time.sleep(3)
        except Exception as e:
            print('open serial  failed.')
        """
    # receive information from USB
    def get_info(self):
        usb_str = ''
        s = self.ser.readline()

        """ if send byte by byte, using '$' to end
        
        if s == b'$':
            break
        else:
            usb_str = usb_str + s.decode('utf-8')
        print("usb receice:" + usb_str)
        return usb_str
        """

        print("usb receice:" + s.decode('utf-8'))
        return s.decode('utf-8')

    # send information to USB
    def put_info(self, info):
        try:
            self.ser.write(info)
            print('usb put:' + info.decode('utf-8'))
        except Exception as e:
            print('failed to put.')
