__author__ = 'mpocciotti'


import boto.ec2
import time

print "Este programa vai checar o status de suas imagens no AWS\n"
print "Estas sao as regioes disponiveis:\n"
regioes = boto.ec2.regions()

# Quais as regioes disponiveis?
for regiao in regioes:
    print regiao
print 'Quantidade de regioes: ',len(regioes), "\n"

# Regiao onde estao as instances
regiao =  'us-west-2'

# Conectando na regiao
ec2_conn = boto.ec2.connect_to_region(regiao)
print boto.ec2.get_region(regiao)
print("")

# Colhendo dados sobre as instances
reservations = ec2_conn.get_all_reservations()
print 'Quantidade de reservations: ',len(reservations)
statuses = ec2_conn.get_all_instance_status()
print reservations, "\n"

# Quais sao as instances que estao rodando? E o status das intances?
print "Instancias rodando:\n"
#print "Reservation:             Instance:             Status:     SecurityGroup: IP Address:\n"

counter = 0
num_instancias_rodando = 0
num_instancias_desligadas = 0
num_instancias_totais = 0

while counter < len(reservations):
    if reservations[counter].instances[0].state == 'running':
        print reservations[counter]
        print reservations[counter].instances[0]
        print 'Status:', reservations[counter].instances[0].state
        print 'Security Group:', reservations[counter].instances[0].groups[0].name
        print 'IP Address:', reservations[counter].instances[0].ip_address, '\n'
        num_instancias_rodando = num_instancias_rodando + 1
    counter = counter + 1

print 'Numero de instances rodando:', num_instancias_rodando
print 'Numero de instances inertes:', len(reservations) - num_instancias_rodando
print 'Numero de instances totais: ', len(reservations)
print

#counter = 0
#while counter < len(reservations):
#    print reservations[counter], ' ', \
#        reservations[counter].instances[0], ' ', \
#        reservations[counter].instances[0].state, '   ', \
#        reservations[counter].instances[0].groups[0].name, ' ', \
#        reservations[counter].instances[0].ip_address
#    counter = counter + 1



