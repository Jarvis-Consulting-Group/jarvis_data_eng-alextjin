#! /bin/bash

psql_host=$1
psql_port=$2
db_name=$3
psql_user=$4
psql_password=$5

#Check # of args
if [ "$#" -ne 5 ]; then
    echo "Illegal number of parameters"
    exit 1
fi

#parse hardware specification
vmstat_mb=$(vmstat --unit M)
hostname=$(hostname -f)
memory_free=$(echo "$vmstat_mb" | awk '{print $4}'| tail -n1 | xargs)
cpu_idle=$(echo "$vmstat_mb" | awk '{print $15}'| tail -n1 | xargs)
cpu_kernel=$(echo "$vmstat_mb" | awk '{print $14}'| tail -n1 | xargs)
disk_io=$(vmstat --unit M -d | tail -1 | awk '{print $10}' | xargs)
disk_available=$(df / -BM | tail -1 | awk '{print $4}' | grep -o '[0-9]\+' | xargs)
timestamp=$(date '+%F %T'| xargs)
host_id="(select id from host_info where hostname = '$hostname';)";


#PSQL command: Inserts server usage data into host_usage table
insert_stmt="INSERT INTO host_usage (timestamp,host_id,memory_free,cpu_idle,cpu_kernel,disk_io,disk_available) (select '$timestamp', id, $memory_free, $cpu_idle, $cpu_kernel, $disk_io, $disk_available from host_info where hostname = '$hostname');"

export PGPASSWORD=$psql_password

psql -h $psql_host -p $psql_port -d $db_name -U $psql_user -c "$insert_stmt"
exit $?
