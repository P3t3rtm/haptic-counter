import struct
import serial
# import io


ser = serial.Serial('COM5', 921600, timeout=0)#,     parity=serial.PARITY_EVEN, rtscts=1)
# ser = serial.Serial('COM5', 9600, timeout=0)


data2 = ""
# while loop 1000 times
i = 0
while i < 100:
    # read data from serial port
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        i = i+1

        data = ser.read(bytesToRead)
        data = data.hex()
        #data = struct.unpack("h", data)
        if data[0:2] == "55":
            data2 = ''
        if len(data) == 22:
            sum = 0
            for i in range(0, 10):
                sum = sum + int(data[i*2:i*2+2], 16)

            # print the hex value of sum
            #print(hex(sum)[3:])

            # if the sum is the same as the 11th hex values, the data is valid
            if hex(sum)[3:] != data[20:22]:
                print("!!!!!Valid data")

            print(data)
            print('data')
        else:
            # store the data in data2 until it is 22 bytes long
            data2 = data2 + data
            if len(data2) == 22:
                # sum up the first 10 hex values
                sum = 0
                for i in range(0, 10):
                    sum = sum + int(data2[i*2:i*2+2], 16)

                # print the hex value of sum
                #print(hex(sum)[3:])

                # if the sum is the same as the 11th hex values, the data is valid
                if hex(sum)[3:] != data2[20:22]:
                    print("!Valid data")

                print(data2)
                print('data2')
                data2 = ""
            # if the data is over 22 bytes long, print the first 22 bytes and set data2 to the rest of the data
            if len(data2) > 22:
                print(data2[0:22])
                print("oversize")
                data2 = data2[22:]
        # else:
        #         #store the data in data2 until it is 22 bytes long
        #         data2 = data2 + data
        #         if len(data2) == 22:
        #             #sum up the first 10 hex values
        #             sum = 0
        #             for i in range(0,10):
        #                 sum = sum + int(data2[i*2:i*2+2],16)
        #             #if the sum is the same as the last 2 hex values, the data is valid
        #             if sum == int(data2[20:22],16):
        #                 print("Valid data")
        #             else:
        #                 print("Invalid data")
        #             print(data2)
        #             print('data2 b')
        #             data2 = ""
        #         #if the data is over 22 bytes long, print the first 22 bytes and set data2 to the rest of the data
        #         if len(data2) > 22:
        #             print(data2[0:22])
        #             print("oversize b")
        #             data2 = data2[22:]

        # #if data starts with 5551 and has 22 length, then print it

        # # if data[0:2] == "55" and len(data) == 22:
        # #     print(data)

        # if data[0:2] == "55" and len(data) == 22:
        #     print(data)

        # #else store data in data2 and print it when data2 has 22 length
        # else:
        #     data2 = data2 + data
        #     if len(data2) == 22:
        #         print(data2)
        #         data2 = ""
        #     #if data2 is over 22 length, print only 22 length, and set data2 to the rest of data
        #     if len(data2) > 22:
        #         print("lghg")
        #         print(data2[0:22])
        #         data2 = data2[22:]


# #while loop 1000 times
# i = 0
# while i < 100:
#     #read data from serial port
#     bytesToRead = ser.inWaiting()
#     if bytesToRead > 0:
#         i=i+bytesToRead

#         data = ser.read(bytesToRead)
#         print(data)
#         if data != b'':
#             print(data)
#             #print(data.hex())


# Serial.print((float)JY901.stcAcc.a[0]/32768*16);
# Serial.print((float)JY901.stcAcc.a[1]/32768*16);
# Serial.println((float)JY901.stcAcc.a[2]/32768*16);


# for i in range(1000):
#     bytesToRead = ser.inWaiting()
#     #read data from serial port
#     data = ser.read(bytesToRead)
#     data = data.hex()
#     if(data != ''):
#         print(data)

    # print data
    # print(data.hex())
    # print(data.decode('utf-8'))
    # print(data.decode('utf-8').split('\r\n'))
    # print(data.decode('utf-8').split('\r\n')[0])
    # print(data.decode('utf-8').split('\r\n')[0].split(','))
    # print(data.decode('utf-8').split('\r\n')[0].split(',')[0])


# while True:
#     bytesToRead = ser.inWaiting()
#     data = ser.read(bytesToRead)
#     #if data is not empty, print it
#     if(ser.read(bytesToRead) != "\'\'" )
#         print(ser.read(bytesToRead))
#     #print(ser.read(bytesToRead))


# ser.close()             # close port
