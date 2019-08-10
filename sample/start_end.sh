ROOTDIR=${PWD}
MODULES=${ROOTDIR}/modules
SAMPLE=${ROOTDIR}/sample

INVISIPORT=${MODULES}/invisiport
PORTSPOOF=${MODULES}/portspoof
SPIDERTRAP=${MODULES}/spidertrap
COWRIE=${MODULES}/cowrie

SCENARIO=${SAMPLE}/scenario
SCENARIO_1=${SCENARIO}/scenario1
SCENARIO_2=${SCENARIO}/scenario2


start()
{
	case $1 in
	1)
		echo "Scenario 1 start : invisiport + spidertrap"		
		sudo python2 $INVISIPORT/invisiport.py -c $SCENARIO_1/config > /dev/null &
		python2 $SPIDERTRAP/spidertrap.py 1> /dev/null 2> /dev/null & 

		;;
	2)
		echo "Scenario 2 start : invisiport + portspoof + cowrie"
		
		sudo python2 $INVISIPORT/invisiport.py -c $SCENARIO_2/config > /dev/null &
		#sudo /etc/init.d/portspoof.sh start
		sudo /usr/local/bin/portspoof -D -c /usr/local/etc/portspoof.conf -s /usr/local/etc/portspoof_signatures &
		source $COWRIE/cowrie-env/bin/activate
		$COWRIE/bin/cowrie start
		#sudo /etc/init.d/portspoof.sh start
		
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
                echo "Scenario 1 end"
		sudo killall python2
		sudo $INVISIPORT/cleanup.sh
		
                ;;
        2)
                echo "Scenario 2 end"
		sudo killall python2
		sudo $INVISIPORT/cleanup.sh
		sudo /etc/init.d/portspoof.sh stop
		source $COWRIE/cowrie-env/bin/activate
		$COWRIE/bin/cowrie stop	

		;;
        3)
                ;;
        *)
                echo "Invalid input"
                ;;
        esac

}



if [ "$1" == "start" ];then
	start $2
elif [ "$1" == "end" ];then
	clean $2
else
	echo "usage : start_end.sh [start|end] [1|2|3]"
fi
