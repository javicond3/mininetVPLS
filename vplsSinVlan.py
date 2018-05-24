"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')
	h4 = self.addHost('h4')
	h5 = self.addHost('h5')
	h6 = self.addHost('h6')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
	

        # Add links
        self.addLink(s1, h1, port1=1, port2=0)
        self.addLink(s2, h2, port1=1, port2=0)
        self.addLink(s3, h3, port1=1, port2=0)
        self.addLink(s4, h4, port1=1, port2=0)
        self.addLink(s5, h5, port1=1, port2=0)
        self.addLink(s6, h6, port1=1, port2=0)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)
        self.addLink(s4, s2)
        self.addLink(s1, s5)
        self.addLink(s4, s5)
        self.addLink(s2, s6)
        self.addLink(s3, s6)
	


topos = { 'vpls': ( lambda: MyTopo() ) }
