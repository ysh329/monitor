#!/usr/bin/python

import time
import commands

def check_service_alive(service_name, inactives=["inactive", "dead"]):
    check_service_cmd = 'service {} status'.format(service_name)
    (check_cmd_status, check_cmd_output) = commands.getstatusoutput(check_service_cmd)
    inact_res = map(lambda inact: inact in check_cmd_output, inactives)
    return False if True in inact_res else True

def restart_service(service_name):
    # run as root, no sudo needed
    restart_service_cmd = "service {} restart".format(service_name)
    (restart_cmd_status, restart_cmd_output) = commands.getstatusoutput(restart_service_cmd)
    print("restart_cmd_status:{}".format(restart_cmd_status)) 
    print("restart_cmd_output:{}".format(restart_cmd_output))
    # TODO run as general user, need sudo and passwd provided 
    '''
    from base64 import decodestring as de
    pswd = ""
    pswd = de(de(pswd))
    print(pswd)
    '''
    return

def monitor_service(service_name, heartbeat_second, _INFO_LEVEL_={"INFO":"INFO", "WARN":"WARN", "ERRO":"ERRO"}):
    while True:
        alive_status = check_service_alive(service_name)
        log_level = _INFO_LEVEL_["INFO"] if alive_status else _INFO_LEVEL_["ERRO"]
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("[{}][{}] service {} alive: {}".\
              format(log_level, current_time, service_name, alive_status))
        time.sleep(heartbeat_second)
        if not alive_status:
            restart_service(service_name)
    return

if __name__ == "__main__":
    # init
    service_name = "mysql"
    heartbeat_second = 300
    monitor_service(service_name, heartbeat_second)
