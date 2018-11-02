# monitor

This little project can monitor service status.

1. Output current service status of `service_name` according your defined time interval `heartbeat_second`;
2. Restart if service `service_name` dead.

## How to Use

You only need to define your service name `service_name` and time interval of alive-check  `heartbeat_second` in code as below:

```python
if __name__ == "__main__":
    # init
    service_name = "mysql"
    heartbeat_second = 300
    monitor_service(service_name, heartbeat_second)
```

Use the following commands to run in the background:

```shell
# method #1
$ python service_monitor.py >> service_monitor.log &

# method #2 if method #1 fail, you can:
$ python service_monitor.py
# type `ctrl+z`, then:
$ bg

# method #3
$ python service_monitor.py &
```

**Caution: run as root user for privileged command.**

If you want to stop this python script, run commands below:

```shell
# find PID of executing service_monitor command
$ ps -u

# kill PID
$ kill <your_service_monitor_pid>
```

## TODO

- Support granting authority for general user for privileged command
- etc.
