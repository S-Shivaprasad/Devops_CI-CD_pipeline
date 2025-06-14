import yaml

def parse_ci_file(file_path):
    with open(file_path, 'r') as stream:
        try:
            content = yaml.safe_load(stream)
            return content
        except yaml.YAMLError as e:
            return {"error": f"YAML parse error: {str(e)}"}

