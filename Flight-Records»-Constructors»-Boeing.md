# Russian Fighter Jets (RU)


### Parameters list
| Parameter name | Presence | Data Type | Unit | Description | Example |
|----------------|----------------|----------|-----------------|-----------------------------------------|---------------|
| timestamp | Required First | Decimal | s | Elapsed time in second since 01/01/1970 | 1583010425910.56 |
| longitude | Required  | Decimal | Decimal Degrees (°)  | Location longitude. Positive values are toward the north and east directions. | 2.9382915 |
| latitude | Required | Decimal | Decimal Degrees (°) | Location latitude. Positive values are toward the north and east directions. | 79.982 |
| altitude | Required | Decimal | Meter (m) | Height above sea level | 2985.9909092 |
| roll | Optional | Decimal | Decimal Degrees (°) | Roll is positive when rolling the aircraft to the right | 0.8 |
| pitch | Optional | Decimal | Decimal Degrees (°) | Pitch is positive when taking-off | 1.5 |
| yaw | Optional | Decimal | Decimal Degrees (°) | Yaw is clockwise relative to the true north | 224.8 |
| u | Optional | Decimal | Meter (m) | Native x coordinate | 1184039.6704352 |
| v | Optional | Decimal | Meter (m) | Native y coordinate | 343628.7183452 |
| heading | Optional | Decimal | Decimal Degrees (°) | Heading is the yaw relative to the true north of the flat world. It is required because the native world north usually does not match spherical world north because of projection errors. | 224.8 |
| air_speed | Required | Decimal | Meter per second (m/s) | Wind speed reported by external sensors  | 516.6514247099457 |
| engine_X | Required | Decimal | Watt (W) | Power of engine number X  | 30565986.61627765 |
| temperature_in | Required | Decimal | Celsius Degree (℃) | Cockpit temperature  | 27.156045641442 |
| humidity_in | Required | Decimal | Percentage (%) | Relative humidity  | 45.971654984 |
| pressure_in | Required | Decimal | Pascal (Pa) | Cockpit pressure  | 27.156045641442 |
| heart_rate | Required | Number | Beats per Minute (bpm) | Pilot's heart beats  | 80 |
| oxygen_mask | Required | Decimal | Percentage (%) | Oxygen concentration sent to the pilot  | 78.3458795665 |

