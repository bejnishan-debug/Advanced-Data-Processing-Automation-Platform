class FileContextManager:
    def __init__(self,file_path,mode):
        self.file_path=file_path
        self.mode=mode
        self.file=None
    def __enter__(self):
            self.file= open(self.file_path,self.mode)
            return self.file
    def __exit__(self, exc_type, exc, tb):
        self.file.close()
    def write_report(file_path, content):
        with FileContextManager(file_path, "w") as file:
            file.write(content)