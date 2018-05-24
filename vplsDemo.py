from mininet.cli import CLI
from mininet.node import Link, Host
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm
from mininet.topo import Topo
from functools import partial

class VLANHost( Host ):
    def config( self, vlan=10, **params ):
        r = super( VLANHost, self ).config( **params )
        intf = self.defaultIntf()        
        self.cmd( 'ifconfig %s inet 0' % intf )       
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )       
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
        newName = '%s.%d' % ( intf, vlan )
        intf.name = newName
        self.nameToIntf[ newName ] = intf
        return r
class VplsTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', cls=VLANHost, vlan=200, mac='00:00:00:00:00:02')
        self.addLink(s1, h1, port1=1, port2=0)
        self.addLink(s2, h2, port1=1, port2=0)
        self.addLink(s1, s2) 
topos = { 'vpls': ( lambda: VplsTopo() ) }
if __name__ == '__main__':
    from onosnet import run
    run(VplsTopo())
