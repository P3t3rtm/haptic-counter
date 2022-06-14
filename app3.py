import serial
import struct
import time

start_time = time.time()

ser = serial.Serial('COM5', 921600, timeout=0)

data2 = ""
count = 0
while count < 1000:
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        count = count+1
        data = ser.read(bytesToRead)
        data = data.hex()
        if data[0:2] == "55":
            data2 = ''

        data2 = data2 + data

        if len(data2) == 22:
            sum = 0
            for i in range(0, 10):
                sum = sum + int(data2[i*2:i*2+2], 16)
            if hex(sum)[3:] == data2[20:22]:
                x = int(struct.unpack(
                    "<h", int(data2[4:8], 16).to_bytes(2, byteorder='big'))[0])
                y = int(struct.unpack(
                    "<h", int(data2[8:12], 16).to_bytes(2, byteorder='big'))[0])
                z = int(struct.unpack(
                    "<h", int(data2[12:16], 16).to_bytes(2, byteorder='big'))[0])
                print("X:", x, "Y:", y, "Z:", z)
            data2 = ""

        if len(data2) > 22:
            sum = 0
            for i in range(0, 10):
                sum = sum + int(data[i*2:i*2+2], 16)
            if hex(sum)[3:] == data[20:22]:
                x = int(struct.unpack(
                    "<h", int(data2[4:8], 16).to_bytes(2, byteorder='big'))[0])
                y = int(struct.unpack(
                    "<h", int(data2[8:12], 16).to_bytes(2, byteorder='big'))[0])
                z = int(struct.unpack(
                    "<h", int(data2[12:16], 16).to_bytes(2, byteorder='big'))[0])
                print("X:", x, "Y:", y, "Z:", z)
            data2 = data2[22:]

print("--- %s seconds --- %s iterations" % (time.time() - start_time, count))
