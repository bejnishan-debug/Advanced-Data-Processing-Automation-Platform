import threading


class ReportThreadService:

    def create_report_thread(self,report_function,*args):
        thread = threading.Thread(target=report_function,args=args)

        thread.start()

        return thread