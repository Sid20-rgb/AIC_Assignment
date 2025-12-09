import pydot
from rdflib import Graph, Namespace


def create_clean_graph(owl_path, output_png="ontology_clean_graph.png"):
    g = Graph()
    g.parse(owl_path)

    ns = Namespace("http://www.example.com/ITS#")

    allowed_predicates = {
        ns.hasOperation,
        ns.hasFormula,
        ns.hasHint,
        ns.hasQuiz,
        ns.hasQuizQuestion,
        ns.questionFromQuiz,
        ns.hasQuizAttempt,
        ns.attemptedQuizBy,
        ns.hasOperationInSession,
        ns.hasShape
    }

    dot = pydot.Dot(graph_type='digraph', rankdir='LR')

    for s, p, o in g:
        if p not in allowed_predicates:
            continue  

        if not (s.startswith(str(ns)) and o.startswith(str(ns))):
            continue

        s_label = s.replace(str(ns), "")
        p_label = p.replace(str(ns), "")
        o_label = o.replace(str(ns), "")

        s_node = pydot.Node(s_label, shape="ellipse", style="filled", fillcolor="#B8D8FF")
        p_node = pydot.Node(p_label, shape="box", style="filled", fillcolor="#FFF2B2")
        o_node = pydot.Node(o_label, shape="ellipse", style="filled", fillcolor="#C7F7C7")

        dot.add_node(s_node)
        dot.add_node(p_node)
        dot.add_node(o_node)

        dot.add_edge(pydot.Edge(s_node, p_node))
        dot.add_edge(pydot.Edge(p_node, o_node))

    dot.write_png(output_png)
    print(f"✔ Clean conceptual RDF graph saved as: {output_png}")


create_clean_graph("its_shape.owl")
