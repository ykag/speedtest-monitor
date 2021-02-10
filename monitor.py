import speedtest
import time
from datetime import datetime


def convert_bps_to_mbps(value):
    return round(value / 1000 / 1000, 1)


spt = speedtest.Speedtest()
spt.get_config()
spt.get_best_server()

while True:
    download = convert_bps_to_mbps(spt.download())
    upload = convert_bps_to_mbps(spt.upload())

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%YT%H:%M:%S")

    print(timestampStr + "," + str(download) + "," + str(upload))
    time.sleep(300)