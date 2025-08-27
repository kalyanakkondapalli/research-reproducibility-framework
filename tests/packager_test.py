import pytest, os
from rrf.packager import create_bundle

def test_create_bundle(tmp_path):
    proj = tmp_path / "project"
    proj.mkdir()
    (proj / "code.py").write_text("print('Hello World')")
    bundle = tmp_path / "bundle.zip"
    create_bundle(str(proj), str(bundle))
    assert bundle.exists()
