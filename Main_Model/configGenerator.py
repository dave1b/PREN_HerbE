from configparser import ConfigParser

# Get the configparser object
config_object = ConfigParser()

# Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["HERBECONFIG"] = {
    "ultrasonicDistanceThresholdInMM": 1000,
    "plantMinProbability": 0.025,
    "restAPIURL": "https://prenh21-dbrunner.enterpriselab.ch/api/v1/updateRun",
    "qrContentOfFinish": "Ziel",
    "afterUltraDetectedRestartHerbETimeInSeconds": 1,
    "shutdownAfterFinishQRcodeTimeInSeconds": 5,
    "cameraContrast": 20,
    "camerExposure": 40,
    "getDistanceIntervalTimeInSeconds": 1,
    "ultrasonicTimeThresholdBetweenInSeconds": 12,
    "distanceTimerInterval": 1,
    "plantIDkey": "",
    "restAPIKey": ""
}

# Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)