from classes.network import Network

server = Network(12345)
server.alert_server("Sending test message")
server.close_connection()
