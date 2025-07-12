def extract_text_from_file(filename, content):
    if filename.endswith((".log", ".txt", ".py")):
        return content
    return "Unsupported file type."