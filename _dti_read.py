import serial

#you may need to change the COM port parameter
ser = serial.Serial('COM10', 9600, timeout=5)

max_reading = 0.000
min_reading = 0.000
delta_min_max = 0.000

while True:
        raw_reading = ser.read(20)
        #print below for debugging
        #print(raw_reading)
        reading = str(raw_reading)
        try:
            reading = str(reading[10:11]) + str(float(reading[13:21])/(1000))
            reading = float(reading)
        except:
            reading = 0

        if reading > max_reading:
            max_reading = reading

        if reading < min_reading:
            min_reading = reading

        delta_min_max = (max_reading - min_reading)

        print("\n"*40)
        print("Current Reading:  {0:.3f}".format(reading))
        print(f"Max Reading: {max_reading:.3f}")
        print(f"Min Reading: {min_reading:.3f}")
        print(f"Delta: {delta_min_max:.3f}")
