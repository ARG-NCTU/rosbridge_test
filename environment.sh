#! /bin/bash

if [ "$1" ]; then

    echo "ROS MASRER $1"

    export ROS_MASTER_URI=http://$1:11311

else

    echo "ROS MASRER 127.0.0.1"

    export ROS_MASTER_URI=http://127.0.0.1:11311

fi



if [ "$2" ]; then

    echo "ROS IP $2"

    export ROS_IP=$2

else

    echo "ROS IP 127.0.0.1"

    export ROS_IP=127.0.0.1

fi


source /opt/ros/melodic/setup.bash
source catkin_ws/devel/setup.bash

# export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/argsubt/multi-husky-goal-navi/catkin_ws/src/real_to_sim_env/model

export GDK_SYNCHRONIZE=1