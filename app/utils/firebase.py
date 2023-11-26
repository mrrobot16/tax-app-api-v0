from db.firebase import firestore

# NOTE: Recursively convert Firebase DocumentReference objects in a nested data structure to dictionaries.
def convert_doc_refs(doc_refs):
    if isinstance(doc_refs, firestore.DocumentReference):
        # Fetch the actual document data if you want
        # Be aware of read costs and handle errors appropriately
        doc = doc_refs.get()
        if doc.exists:
            doc_data = doc.to_dict()
            # Here, we apply convert_doc_refs recursively on the fetched data
            return convert_doc_refs(doc_data)
        else:
            return None  # Handle non-existing documents as you see fit
    elif isinstance(doc_refs, list):
        # Handle lists by applying the function recursively to each element
        return [convert_doc_refs(item) for item in doc_refs]
    elif isinstance(doc_refs, dict):
        # Handle dictionaries by applying the function recursively to each value
        return {key: convert_doc_refs(value) for key, value in doc_refs.items()}
    else:
        # For any other type, return the doc_refs as is
        return doc_refs