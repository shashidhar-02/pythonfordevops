server_config={
    'server1':{'ip':'192.168.1.100','port':8080,'status':'active'},
    'server2':{'ip':'192.168.1.101','port':8000,'status':'inactive'},
    'server3':{'ip':'192.168.1.102','port':9000,'status':'active'}
}
def get_server_status(server_name):
    return server_config.get(server_name,{}).get('status','server not found')
print(get_server_status('server1'))
server_name='server2'
status=get_server_status(server_name)
print(f"{server_name} status:{status}")