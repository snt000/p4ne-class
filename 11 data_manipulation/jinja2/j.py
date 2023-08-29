from jinja2 import Environment, FileSystemLoader

#Give the location of the .j2 template
file_loader = FileSystemLoader('./jinja-templates')
env = Environment(loader=file_loader)

#Setting up the variables for all our routers
routerlist = [
    {
        "hostname":"DR101",
        "localasn":"33915",
        "bgp_neighbor":"192.168.22.1",
        "remote_asn":"65222"
    },
    {
        "hostname":"DR102",
        "localasn":"33916",
        "bgp_neighbor":"192.168.22.2",
        "remote_asn":"65223"
    }
]

#Gets the j2 template
template = env.get_template('router-template.j2')

#Loop round for each router
for router in routerlist:
    print ("----------------------------")
    
    #Merge the variables with the j2 file
    output = template.render(**router)

    #Rather than save the config file lets just print
    print(output)
    print ("----------------------------")