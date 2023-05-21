# NanoLeafCLI
Simple CLI to set nanoleaf panel effects

## config.json
Simple JSON file to go in the top level, pretty self explanatory. Brightness is a value 0-100, colour specified with RGB
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
