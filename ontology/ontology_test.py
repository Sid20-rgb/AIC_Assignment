from ontology_loader import OntologyLoader

def run_ontology_tests():
    print("=== Ontology Integration Test ===\n")

    try:
        onto = OntologyLoader("its_shape.owl")
        print("✔ Ontology loaded successfully.\n")
    except Exception as e:
        print("✘ Failed to load ontology:", e)
        return

  
    tests = [
        ("Square", "Area"),
        ("Square", "Perimeter"),
        ("Rectangle", "Area"),
        ("Rectangle", "Perimeter"),
        ("Triangle", "Area"),
        ("Triangle", "Perimeter"),
        ("Circle", "Area"),
        ("Circle", "Perimeter"),
    ]

    for shape, operation in tests:
        formula = onto.get_formula(shape, operation)
        print(f"{shape} {operation} Formula → {formula}")

    print("\n=== Test Completed ===")

if __name__ == "__main__":
    run_ontology_tests()
