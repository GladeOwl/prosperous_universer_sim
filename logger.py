FILE_NAME = "simulation_logs.md"


def create_log():
    with open(FILE_NAME, "w") as txtf:
        txtf.write("Log Start")


def write_to_log(text):
    with open(FILE_NAME, "a") as txtf:
        txtf.write("\n")
        txtf.write(text)


def add_partition():
    with open(FILE_NAME, "a") as txtf:
        txtf.write("\n")
        txtf.write("------------------")
