# Introduction

This project aims to reduce the Linux Cluster Administration (LCA) team workload by designing a script to track the instance performance. The LCA team is responsible for monitoring the performance of our Linux platform. It needs to record both the hardware specifications of each node and the node resource in real time. Therefore, I developed a minimum viable product for testing purposes. So I can identify its functionality and the potential for improvement.

I used docker to implement and test the design as it is a cost-efficient and handy approach which could ensure the script can run consistently regardless of where it is. To ease the docker setup and control, the 'psql_docker.sh' helps users to create and trigger the container. Also, the 'ddl.sql' defined the tables' structure, which has sufficient but not too much information for analytic purposes. To x`, 'host_info.sh' and 'host_usage.sh' will extract the details from the Linux platform. The resources usage script is scheduled with crontab to collect the data continuously and minimise all unnecessary manual involvement. All the related data will be stored in the PSQL instance for data analytics purposes in the future. I used Git as the version control tool for this project, and all the related scripts are accessible on GitHub.

# Quick Start
Here are some commands to trigger the scripts.
- Start a psql instance using psql_docker.sh. 
    ```
    psql_docker.sh start
    ```
- Create tables using ddl.sql
    ```
    psql -h localhost -U postgres -d host_agent -f ddl.sql
    ```
- Insert hardware specs data into the DB using host_info.sh
    ```
    # Script usage
    host_info.sh psql_host psql_port db_name psql_user psql_password

    ## Example
    host_info.sh localhost 5432 host_agent postgres mypassword
    ```
- Insert hardware usage data into the DB using host_usage.sh
    ```
    bash scripts/host_usage.sh localhost 5432 host_agent postgres password
    ```
- Crontab setup
    ```
    # edit crontab
    crontab -e

    #adding the job crontab
    * * * * * /home/centos/dev/jarvis_data_eng_alex/linux_sql/scripts/host_usage.sh localhost 5432 host_agent postgres password > /tmp/host_usage.log
    ```

# Implemenation
## Architecture
Draw a cluster diagram with three Linux hosts, a DB, and agents (use draw.io website). Image must be saved to the `assets` directory.

## Scripts
Shell script description and usage (use markdown code block for script usage)
- psql_docker.sh
    > This script is designed to set up a psql instance using docker. User can rather create, start or stop the container.
     ```
    # script usage
    psql_docker.sh start stop|create [db_username][db_password]

    # examples
    ## create a psql docker container with the given username and password.
    psql_docker.sh create db_username db_password

    ## start the stoped psql docker container
    psql_docker.sh start

    ## stop the running psql docker container
    psql_docker.sh stop
    ```
- host_info.sh
    > This script collects hardware specification data and then inserts the data into the psql instance.
    ```
    # Script usage
    ./scripts/host_info.sh psql_host psql_port db_name psql_user psql_password

    # Example
    ./scripts/host_info.sh "localhost" 5432 "host_agent" "postgres" "mypassword"
    ```
- host_usage.sh
    > This script collects server usage data and then inserts the data into the psql database
    ```
    # Script usage
    bash scripts/host_usage.sh psql_host psql_port db_name psql_user psql_password

    # Example
    bash scripts/host_usage.sh "localhost" 5432 "host_agent" "postgres" "mypassword"
    ```
- crontab
    ```
    #edit crontab jobs
    crontab -e

    #add this to crontab
    * * * * *  bash /home/centos/dev/jarvis_data_eng_alex/linux_sql/scripts/host_usage.sh localhost 5432 host_agent postgres password > /tmp/host_usage.log

    #list crontab jobs
    crontab -l
    ```
- queries.sql (describe what business problem you are trying to resolve) #to be updated
    ```
    ```

## Database Modeling
Describe the schema of each table using markdown table syntax (do not put any sql code)
- `host_info`
    | Column Name | Data Type | Nullable|
    | ----------- | ----------- |-----------|
    | id | SERIAL | NOT NULL|
    | hostname | VARCHAR | NOT NULL|
    | cpu_number| INT2 | NOT NULL|
    | cpu_architecture| VARCHAR | NOT NULL|
    | cpu_model| INT2 | NOT NULL|
    | cpu_mhz| VARCHAR | NOT NULL|
    | l2_cache| FLOAT8 | NOT NULL|
    | timestamp| TIMESTAMP | NOT NULL|
    | total_mem| INT4 | NOT NULL|
- `host_usage`
    | Column Name | Data Type | Nullable|
    | ----------- | ----------- |-----------|
    | timestamp | TIMESTAMP | NOT NULL|
    | host_id | SERIAL | NOT NULL|
    | memory_free| INT4 | NOT NULL|
    | cpu_idle| INT2 | NOT NULL|
    | cpu_kernel| INT2 | NOT NULL|
    | disk_io| INT4 | NOT NULL|
    | disk_available| INT4 | NOT NULL|
# Test
The bash script testing is done with mutiple trial runs, including valid & invalid cases. Only inputting appropiate parameters will lead to a desirable result. Otherwise, all the results should return error.

# Deployment
`host_usage` is scheduled in crontab to data collection purposes. All the relevant scripts are deployed in Github. 

# Improvements
- support multiple database options
- provide analysed reports by views
- send email alert when daily job run failed
