import zmq
from pydicom import dcmread
from pydicom.errors import InvalidDicomError
from pydicom.filebase import DicomBytesIO

# ZeroMQ context
context = zmq.Context()

# Socket for receiving messages
receiver = context.socket(zmq.SUB)

# Connect to the server
receiver.connect("tcp://server:5555")

# Set the topic
topic = ""
receiver.setsockopt(zmq.SUBSCRIBE, topic.encode())

while True:
    # Receive data from the server
    data = receiver.recv()
    # Convert the received data to a pydicom Dataset
    try:
        ds = dcmread(DicomBytesIO(data))
        print(ds)
    except InvalidDicomError:
        print("Received non-DICOM data")
        continue
