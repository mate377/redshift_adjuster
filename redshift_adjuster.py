import yaml
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Calls redshift to change redness \
of the screen, keeping track of the value')
parser.add_argument('action', type=str, choices=['increase','decrease','restore','print'],
                    help='change the redshift by the standard amount')
args = parser.parse_args()

stream_conf=open("config.yaml","r")
stream_current=open("current.yaml","r+")

config=yaml.load(stream_conf, Loader=yaml.FullLoader)
current=yaml.load(stream_current, Loader=yaml.FullLoader)

if(args.action=='increase'):
    current['redshift_value']=current['redshift_value']+config['redshift_increment']
elif(args.action=='decrease'):
    current['redshift_value']=current['redshift_value']-config['redshift_increment']
elif(args.action=='restore'):
    current['redshift_value']=config['redshift_base_value']
else:
    pass
subprocess.run(['redshift', '-PO', str(current['redshift_value'])],capture_output=True)
stream_current.seek(0)
stream_current.truncate()
yaml.dump(current,stream=stream_current)
print(current['redshift_value'])

'''
#print(os.listdir())
stream_conf=open("config.yaml","r")
stream_current=open("current.yaml","r+")
#stream_exp=open("fff.yaml","w")

config=yaml.load(stream_conf, Loader=yaml.FullLoader)
current=yaml.load(stream_current, Loader=yaml.FullLoader)

print(current['redshift_value'])


subprocess.run(['redshift', '-PO', str(current['redshift_value'])])
'''
