ROOTDIR=${PWD}
MODULES=${ROOTDIR}/modules

INVISIPORT=${MODULES}/invisiport
PORTSPOOF=${MODULES}/portspoof
SPIDERTRAP=${MODULES}/spidertrap
COWRIE=${MODULES}/cowrie

start()
{
	case $1 in
	1)
		echo "Scenario 1 start : portspoof + spidertrap"		
		
		;;
	2)
		echo "Scenario 2 start : invisiport + portspoof + cowrie"
		
		sudo python2 $INVISIPORT/invisiport.py -c $INVISIPORT/config > /dev/null &
		sudo /etc/init.d/portspoof start
		
		;;
	3)
		;;
	*)
		echo "Invalid input"
		;;
	esac
}


clean()
{
        case $1 in
        1)
                echo "Scenario 1 end : clean iptalbes"
                ;;
        2)
                echo "Scenario 2 end : clean iptables"
                sudo $INVISIPORT/cleanup.sh
		
		;;
        3)
                ;;
        *)
                echo "Invalid input"
                ;;
        esac

}



if [ x$1 == x ]; then
	echo "usage : start_end.sh [start|end] [1|2|3]"
elif [ $1 == "start" ]; then
	start $2
elif [ $1 == "end" ]; then
	clean $2
fi
