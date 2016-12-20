from azure.servicebus import ServiceBusService, Message, Queue

#sudo pip install azure bzw. nur den azure-servicebus damit es schneller gehtS
service_namespace = 'svpservicebus'
key_name = 'PiKey' # SharedAccessKeyName from Azure portal
key_value = 'uFAnfl9Js5ELJ/1n3xoB39uVvshmhEXdUzLEStdfW0c=' # SharedAccessKey from Azure portal
connectionString = 'Endpoint=sb://svpservicebus.servicebus.windows.net/;SharedAccessKeyName=Reader;SharedAccessKey=smSDkgYnikYSZ9ia07p5i7/uzSdcH9zOdeIJoKfhPng=;EntityPath=iot-maker-lab01-queue'

bus_service = ServiceBusService(service_namespace,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

#bus_service.create_queue('iot-maker-lab01-queue')
#sb://svpservicebus.servicebus.windows.net/

decide = raw_input("Anlegen [1], Auslesen [2], Abbrechen [3]: ")

while decide != "3":
    if decide == "1":
        msg_body = raw_input("Bitte geben Sie ihren Namen ein: ")
        msg = Message(b'Hallo, '+msg_body)
        bus_service.send_queue_message('iot-maker-lab01-queue', msg)
    elif decide == "2":
        msg = bus_service.receive_queue_message('iot-maker-lab01-queue', peek_lock=False)
        print(msg.body)
    decide = raw_input("Anlegen [1], Auslesen [2], Abbrechen [3]: ")
