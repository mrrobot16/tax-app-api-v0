from app.db.firebase import FIREBASE_CREDENTIALS, firestore_db, credentials

def test_firebase_credentials_values():
    assert isinstance(FIREBASE_CREDENTIALS, dict)
    assert isinstance(FIREBASE_CREDENTIALS['type'], str)
    assert isinstance(FIREBASE_CREDENTIALS['project_id'], str)
    assert isinstance(FIREBASE_CREDENTIALS['private_key'], str)
    assert isinstance(FIREBASE_CREDENTIALS['client_email'], str)
    assert isinstance(FIREBASE_CREDENTIALS['token_uri'], str)

def test_firebase_credentials_attributes():
    expected_attributes = [
        'get_access_token',
        'get_credential',
        'project_id',
        'service_account_email',
        'signer'
    ]
    for attr in expected_attributes:
        assert hasattr(credentials, attr), f"Credentials object missing attribute: {attr}"

def test_firestore_db_attributes():
    expected_attributes = [
        'SCOPE',
        'batch',
        'bulk_writer',
        'close',
        'collection',
        'collection_group',
        'collections',
        'document',
        'field_path',
        'from_service_account_info',
        'from_service_account_json',
        'get_all',
        'project',
        'recursive_delete',
        'transaction',
        'write_option'
    ]

    for attr in expected_attributes:
        assert hasattr(firestore_db, attr), f"Client object missing attribute: {attr}"