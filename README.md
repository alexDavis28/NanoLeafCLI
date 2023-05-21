# NanoLeafCLI
Simple CLI to set nanoleaf panel effects

## config.json
JSON file to go in the top level, pretty self explanatory - if you haven't created it already the script will create it.
nanoleafip is the local IP address of your panels, each listed effect is a static effect.
The panels can't be set to a static effect by name and as such they have to be manually specified.
Brightness is a value 0-100, colour specified with RGB
```json
{
   "nanoleafIP":"192.168.0.10",
   "effects":{
      "Concentrate":{
         "red":217,
         "green":192,
         "blue":173,
         "brightness":65
      },
      "Evening":{
         "red":245,
         "green":183,
         "blue":91,
         "brightness":50
      },
      "Reading":{
         "red":247,
         "green":200,
         "blue":119,
         "brightness":75
      }
   }
}
```
## Authentication
Before running the script for the first time hold the power button on your nanoleaf device for 5 to 7 seconds so that an authentication token will be generated.
Otherwise, you'll see a NanoleafRegistrationError teling you this.
