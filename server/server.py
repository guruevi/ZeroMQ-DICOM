import os
import zmq

# ZeroMQ context
context = zmq.Context()

# Socket for sending messages
sender = context.socket(zmq.PUB)

# Bind the socket to the port
sender.bind("tcp://*:5555")

# The directory to watch
watch_dir = './watch'

# The files that have already been sent
sent_files = set()

while True:
    # Get a list of all files in the watch directory
    files = os.listdir(watch_dir)
    for file in files:
        file_path = os.path.join(watch_dir, file)
        if file not in sent_files:
            # Send the file to the receivers
            print(f"Sending {file}")
            with open(file_path, 'rb') as f:
                data = f.read()
                sender.send(data, zmq.NOBLOCK)
            sent_files.add(file)
            print(f"Sent {file}")