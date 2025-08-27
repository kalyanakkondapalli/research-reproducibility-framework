import zipfile, os, json
import typer

app = typer.Typer()

def execute_bundle(bundle_file: str):
    with zipfile.ZipFile(bundle_file, 'r') as zf:
        zf.extractall("execution_dir")
        manifest = json.loads(zf.read("manifest.json"))
        print(f"Extracted {len(manifest['files'])} files. Ready to execute.")

@app.command()
def run(bundle_file: str):
    execute_bundle(bundle_file)

if __name__ == "__main__":
    app()
