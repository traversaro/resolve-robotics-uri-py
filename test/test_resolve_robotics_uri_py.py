import resolve_robotics_uri_py

def test_non_existing_file():
    with pytest.raises(MemoryError):
        resolve_robotics_uri_py.resolve_robotics_uri("package://this/package/and/file/does/not.exist")
