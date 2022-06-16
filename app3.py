from numpy import sqrt
import serial
import struct
import time
from matplotlib import pyplot as pp

start_time = time.time()

ser = serial.Serial('COM9', 921600, timeout=0)

# # set the rate
# ser.write(bytes.fromhex('FFAA6988B5'))
# ser.write(bytes.fromhex('FFAA030c00'))
# ser.write(bytes.fromhex('FFAA000000'))

data2 = ""
count = 0
guess = 0 


# plot 
magnitude_list = []

threshold = 30000
baseline = 0
baselinethreshold =5000

while count < 5500:
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        count = count+1
        data = ser.read(bytesToRead)
        data = data.hex()
        
        if data[0:4] == "5551":
            data2 = ''

        data2 = data2 + data

        if len(data2) >= 22:
            sum = 0
            for i in range(0, 10):
                sum = sum + int(data2[i*2:i*2+2], 16)
            if hex(sum)[3:] == data2[20:22] and data2[0:4] == "5551":
                x = int(struct.unpack(
                    "<h", int(data2[4:8], 16).to_bytes(2, byteorder='big'))[0])
                y = int(struct.unpack(
                    "<h", int(data2[8:12], 16).to_bytes(2, byteorder='big'))[0])
                z = int(struct.unpack(
                    "<h", int(data2[12:16], 16).to_bytes(2, byteorder='big'))[0])
                # print("X:", x/32768*16, "Y:", y/32768*16, "Z:", z/32768*16)
                # print("Xd:", x-x1, "Yd:", y-y1, "Zd:", z-z1)
                magnitude = sqrt((x*x) + (y*y) + (z*z))
                magnitude_list.append(magnitude)
                if magnitude < baselinethreshold:
                    baseline = 1

                if magnitude > threshold and baseline == 1:
                    guess+=1
                    print("X:", x, "Y:", y, "Z:", z, "|| Magnitude: ||", magnitude)
                    baseline = 0
            data2 = data2[22:]

# plot the output in mpl
figure, axes = pp.subplots()
axes.plot(magnitude_list, color='green')
axes.set_title("Guess: " + str(guess))
pp.show()

print("--- %s seconds --- %s iterations" % (time.time() - start_time, count))

print("Guess:", guess)

