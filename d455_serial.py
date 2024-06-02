import pyrealsense2 as rs

# Realsense 장치의 context를 생성
context = rs.context()

# 연결된 모든 장치를 나열
devices = context.query_devices()

# 각 장치의 정보를 출력
for i, device in enumerate(devices):
    print(f"Device {i}:")
    print(f"  Name: {device.get_info(rs.camera_info.name)}")
    print(f"  Serial number: {device.get_info(rs.camera_info.serial_number)}")
    print(f"  Firmware version: {device.get_info(rs.camera_info.firmware_version)}")


# (efficientvit) libra@libra:~/git/RoboEXP$ /home/libra/anaconda3/envs/efficientvit/bin/python /home/libra/git/RoboEXP/d455_serial.py
# Device 0:
#   Name: Intel RealSense D455
#   Serial number: 309622300987
#   Firmware version: 5.13.0.55