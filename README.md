# tnc-proxy
Proxy for TNC KISS like direwolf, soundmodem, etc.

When you use APRS application with direwolf you have only active connection and it's working like a charm. But what when you connect to direwolf more programs at once? Where one application sends data to direwolf other applications doesn't see this data.

This scripts connects to direwolf and setup listening port to other application (like APRX, APRSIS32, etc). If any, from connected application, sends data this data will be sent to other connected application.

# How to use:
- open file,
- edit lines 8,9 to setup listening port and IP (where application will be connecting),
- edit lines 11, 12 to point to direwolf,
- run ./tnc_proxy.py
