# ZeroMQ-DICOM
This is a proof of concept to show the distribution of DICOM images for a RT-MRI (Real-Time Magnetic Resonance Imaging) system to multiple clients.

As the scanner writes individual images after each TR to the /watch directory, this system will pick each new image up, send them using ZeroMQ to all 
clients. 

At this point, our scanner only supports depositing the data on a Samba share. The Samba share the scanner deposits data to, should run on the same 
server as the server.py process (you can implement the necessary fileshare using eg. dperson/samba in the docker-compose.yml file)

The images should be small enough or the entire system fast enough to send them and process the data within the cycle. Clients could lose images if they 
aren't fast enough to process, so using a multi-threaded client paradigm may be necessary to service all images. Tested with 50 100k images/second (5MB/s)
on a sufficiently modern system with a 10G network without any losses.

* The server is using 100% CPU *
Yes, the server.py process consumes 100% of a single thread because it continuously scans the local directory for changes. You can avoid that by inserting 
a sleep, but then you run the risk that some of your data is slightly delayed.

* Why not use inotify *
inotify doesn't work between Docker containers, inotify is also not 100% reliable. However using it would solve the previous issue. Perhaps using a filter
on the Samba log (make sure logs are created for each file written) may be a solution, haven't tested any reliability or delay issues that may occur.\

* Why not use another MQ platform *
Complexity and performance primarily. If there are other platforms that are as fast or faster than ZeroMQ and offer functionality you like, feel free to 
submit patches.
