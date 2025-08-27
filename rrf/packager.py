import zipfile, os, json, yaml
import typer

app = typer.Typer()

def create_bundle(input_dir: str, output_file: str):
    manifest = {"files": [], "dependencies": [], "python_version": f"{os.sys.version}"}
    with zipfile.ZipFile(output_file, 'w') as zf:
        for root, dirs, files in os.walk(input_dir):
            for f in files:
                filepath = os.path.join(root, f)
                zf.write(filepath, arcname=os.path.relpath(filepath, input_dir))
                manifest["files"].append(os.path.relpath(filepath, input_dir))
        zf.writestr("manifest.json", json.dumps(manifest, indent=2))
    print(f"Bundle created: {output_file}")

@app.command()
def pack(input_dir: str, output_file: str):
    create_bundle(input_dir, output_file)

if __name__ == "__main__":
    app()
