#!/usr/bin/env python3

import can
import time
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000
from can.interface import Bus

def send_one():
    with can.Bus() as bus:
        msg = can.Message(
            arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True
        )
        file1 = open("file.txt", "a")
        try:
            while True:
                file1.write(str(msg)+"\n")
                file1.flush()
                bus.send(msg)
                print(f"Message sent on {bus.channel_info}")
                time.sleep(1)
        except can.CanError:
            print("Message NOT sent")


if __name__ == "__main__":
    send_one()