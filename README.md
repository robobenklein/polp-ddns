
# PoLP DDNS Service

Principle of Least Privilege Dynamic DNS server.

Most DDNS client implementations are designed to figure out their own IP and use an auth token to update a specific record in a DNS service.

The problem with this approach is that the system requires access to update the record to any value they desire, and often the access token is not specific enough to allow write access to only a single record.

And of course I don't want to create separate access tokens for every machine's IP I want to track (think IPv6 public addresses) so ideally I shouldn't have to install a new app on every device.

## The Approach

So here's a new approach to DDNS, requiring just one HTTPS server and just a curl cronjob on the clients you want to track.

In this case the server does not require any data from the machine besides the request, since the server will update the IP to where it sees the request is coming from.
