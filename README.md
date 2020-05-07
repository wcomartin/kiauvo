# Kia Uvo

API Wrapper for the Kia Uvo service

This Wrapper was created for use with the Home Assistant integration, your usage may vary, feel free to contribute


# Usage

```python
from KiaUvo import KiaUvo

client = KiaUvo("username/email", "password")
client.login()

# To see available vehicles
client.get_vehicle_list()

# to select a vehicle for the rest of the methods
client.select_vehicle("vehicle id", "pin")
```

# Available Methods

| Method | Description | 
| --- | --- |
| `verify_token()` | Used to verify the token is still valid if not login again |
| `verify_pin()` | Check to see the pin is correct |
| `select_vehicle()` | Sets the private vehicle_id property for use with other methods |
| `get_vehicle_list()` | gets a list of available vehicles on the account |
| `get_vehicle_status()` | gets all of the last known data for the vehicle from kia servers |
| `request_vehicle_update()` | forces a refresh from the kia servers to the vehicle, this has a limiter, the number of requests per day is unknown |
| `start_vehicle(preset)` | sends the start command to the vehicle, requires a preset from the vehicle status |
| `stop_vehicle()` | sends the stop command to the vehicle |
| `lock_vehicle()` | sends the lock command to the vehicle |
| `unlock_vehicle()` | sends the unlock command to the vehicle |
| `find_my_vehicle()` | does not work, if anyone can figure out why that'd be great. |