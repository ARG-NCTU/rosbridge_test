# -*- coding: utf-8 -*-
import roslibpy
import time

def println(ros_list):
    if len(ros_list) == 0:
        print('Empty')
    else:
        for i in ros_list:
            print(i)
    return 0

host = '192.168.50.177'

client = roslibpy.Ros(host = host, port = 9090)
client.run()
print('Is ROS connected?', client.is_connected)

while True:
    message_data = input('what message you want to publish')
    talker = roslibpy.Topic(client, '/no_ros_publish', 'std_msgs/String')
    for i in range(1,100):
        talker.publish(roslibpy.Message({'data': message_data}))
        print('Sending message...')
        time.sleep(1)
    talker.unadvertise()
    client.terminate()
