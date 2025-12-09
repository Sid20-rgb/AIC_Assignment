from rdflib import Graph, Namespace, URIRef


class OntologyLoader:
    def __init__(self, owl_path):
        self.graph = Graph()
        self.graph.parse(owl_path)

        self.ns = Namespace("http://www.example.com/ITS#")

    def get_formula(self, shape_name: str, operation: str):

        shape_uri = self.ns[f"{shape_name}_1"]   # e.g., Square_1
        op_uri = self.ns[f"{shape_name}{operation}_Operation"]

        if (shape_uri, self.ns.hasOperation, op_uri) not in self.graph:
            return f"No {operation} formula found for {shape_name}"

        formula_uri = self.graph.value(subject=op_uri, predicate=self.ns.hasFormula)

        if formula_uri is None:
            return "Formula missing in ontology."

        formula_text = self.graph.value(subject=formula_uri, predicate=self.ns.formulaText)

        if formula_text:
            return str(formula_text)

        return "Formula not found."
