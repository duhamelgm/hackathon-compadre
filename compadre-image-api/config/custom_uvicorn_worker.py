from uvicorn.workers import UvicornWorker


class CustomUvicornWorker(UvicornWorker):
    def init_process(self):
        self.cfg.uvicorn_config = "uvicorn_conf.py"
        super().init_process()
