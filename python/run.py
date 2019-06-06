import urllib3
import os
import simulation_methods
import command_line_args

from cohesity_wrapper.cohesity import get_s3_keys

if __name__ == "__main__":
    configuration = command_line_args.handler.handler()

    os.system("../scripts/generate_test_cases.sh")

    if configuration.method == "individual":
        if configuration.communication == "write":
            print("Individual | Write")
            simulation_methods.individual.write(configuration)
        if configuration.communication == "read":
            print("Individual | Read")
            # simulation_methods.individual.read()
    elif configuration.method == "concurrent":
        if configuration.communication == "write":
            print("Concurrent | Write")
            # simulation_methods.concurrent.write()
        if configuration.communication == "read":
            print("Concurrent | Read")
            # simulation_methods.concurrent.read()
    elif configuration.method == "paralell":
        if configuration.communication == "write":
            print("Parallel | Write")
            # simulation_methods.paralell.write()
        if configuration.communication == "read":
            print("Parallel | Read")
            # simulation_methods.paralell.read()
    else:
        raise Exception("Bad input |", configuration)