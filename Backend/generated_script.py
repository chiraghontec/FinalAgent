from manim import *

class ThreeWayHandshake(Scene):
    def construct(self):
        # Create host nodes
        client = Circle(color=BLUE, radius=0.5).shift(LEFT * 4)
        server = Circle(color=BLUE, radius=0.5).shift(RIGHT * 4)

        # Add labels to hosts
        client_label = Text("Client", color=WHITE).next_to(client, DOWN)
        server_label = Text("Server", color=WHITE).next_to(server, DOWN)

        # Create messages arrows
        syn = Arrow(client.get_center(), server.get_center(), buff=0.5)
        syn_label = Text("SYN", color=YELLOW).next_to(syn, UP)

        syn_ack = Arrow(server.get_center(), client.get_center(), buff=0.5)
        syn_ack_label = Text("SYN-ACK", color=YELLOW).next_to(syn_ack, UP)

        ack = Arrow(client.get_center(), server.get_center(), buff=0.5)
        ack_label = Text("ACK", color=YELLOW).next_to(ack, UP)

        # Add elements to the scene
        self.play(Write(client), Write(client_label))
        self.play(Write(server), Write(server_label))

        # Perform handshake animations
        self.play(Create(syn), Write(syn_label))
        self.wait(1)
        self.play(Create(syn_ack), Write(syn_ack_label))
        self.wait(1)
        self.play(Create(ack), Write(ack_label))
        self.wait(2)

# To preview the animation, save this script as `filename.py` and run the following command:
# manim -pql filename.py ThreeWayHandshake