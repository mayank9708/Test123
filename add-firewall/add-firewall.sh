#!/bin/bash
sudo systemctl status iptables &> /dev/null
if [ $? = 0 ];then
        echo "iptable running"
        echo "You can add rules now!!!"
        echo "Enter source IP (Single IP or Network IP)"
        read src
        echo "Enter destination Website or Network IP"
        read dst
        echo "Specify destination port"
        read dstp
        echo "Enter protocol"
        read proto
        echo "Enter target/action"
        read target

        echo "Adding command"
        sudo iptables -I FORWARD 1 -p $proto -s $src -d $dst --dport $dstp -j $target
        sudo iptables -I FORWARD 2 -p $proto -d $src -s $dst --sport $dstp -j $target
        echo "Sucessfull!!!!!!!!!!"
else
        echo "iptable not running"
        sudo systemctl start iptables &> /dev/null
        if [ $? = 0 ];then
                echo "Now iptable started"
        fi
fi

