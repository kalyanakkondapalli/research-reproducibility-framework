# Example CI/CD integration hooks
def ci_scan(bundle_file: str):
    from runner import execute_bundle
    print("Running reproducibility CI scan...")
    execute_bundle(bundle_file)
