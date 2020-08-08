import argparse
import time
import sys

try:
    import kismetexternal
except ImportError:
    print("ERROR:  Kill Endpoint Plugin requires the kismetexternal python library;")
    print("        you can find it in the kismetexternal git or via pip")
    sys.exit(1)

try:
    import psutil
except ImportError:
    print("ERROR:  Kill Endpoint Plugin requires module psutil be installed")
    sys.exit(1)


def kill_processes(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            print("killing process id {}".format(process.pid))
            process.kill()


class KillEndpoint(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Kill Endpoint Plugin")

        self.parser.add_argument("--in-fd", action="store", type=int, dest="infd")
        self.parser.add_argument("--out-fd", action="store", type=int, dest="outfd")

        self.results = self.parser.parse_args()

        if self.results.infd is None or self.results.outfd is None:
            print("ERROR:  Kill Endpoint Plugin should be launched by Kismet itself;")
            print("        running it on its own won't do what you want")
            sys.exit(1)

        self.kei = kismetexternal.ExternalInterface(
            self.results.infd, self.results.outfd
        )

        # self.kei.debug = True

        self.kei.start()

        self.kei.add_uri_handler("GET", "/kill.cmd", self.handle_uri)

        self.kei.run()

    def handle_uri(self, externalhandler, request):
        externalhandler.send_http_response(
            request.req_id,
            bytes(
                "<html><body>Killing process</body></html>",
                "UTF-8",
            ),
        )

        kill_processes("kismet")

    def loop(self):
        while self.kei.is_running():
            self.kei.send_ping()
            time.sleep(1)

        self.kei.kill()


def main():
    kill_endpoint = KillEndpoint()
    kill_endpoint.loop()


if __name__ == "__main__":
    main()
