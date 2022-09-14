import string

FILE_NAME = "simulation_logs.md"


def create_log():
    with open(FILE_NAME, "w") as txtf:
        txtf.write("Log Start")


def write_to_log(time: tuple, entity: string, text: string):
    with open(FILE_NAME, "a") as txtf:
        txtf.write(f"\n[{time[0]}D:{time[1]}H:{time[2]}M] [{entity}] {text}")


def write_text_to_log(text: string):
    with open(FILE_NAME, "a") as txtf:
        txtf.write(f"\n{text}")


def add_partition():
    with open(FILE_NAME, "a") as txtf:
        txtf.write("\n")
        txtf.write("------------------")
