from graph import Vertex

BOS = Vertex("BOS", 50, 60)
JFK = Vertex("JFK", 85, 11)
SFO = Vertex("SFO", 9 ,58)
ORD = Vertex("ORD", 95, 22)
MIA = Vertex("MIA", 83, 39)
DFW = Vertex("DFW", 91, 73)
LAX = Vertex("LAX", 60, 98)

list_vertices = [BOS, JFK, SFO, ORD, MIA, DFW, LAX, BOS]

X = [vertex.horizon for vertex in list_vertices]
y = [vertex.vertical for vertex in list_vertices]

label_vertices = [vertex.element for vertex in list_vertices]

vertices = {
    BOS: [SFO, JFK, MIA, ORD, DFW, LAX],
    JFK: [BOS, SFO, ORD, DFW, MIA, LAX],
    SFO: [BOS, JFK, DFW, ORD, MIA, LAX],
    ORD: [BOS, JFK, SFO, LAX, DFW, MIA],
    MIA: [BOS, JFK, SFO, DFW, ORD, LAX],
    DFW: [BOS, SFO, JFK, ORD, MIA, LAX],
    LAX: [BOS, JFK, SFO, ORD, DFW, MIA]
}
