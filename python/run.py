import simulation_methods, command_line_args
import urllib3

urllib3.disable_warnings()

if __name__ == "__main__":
    configuration = command_line_args.handler.handler()

    print("INFO:\tPlatform: {}\tMethod: {}\tCommunication: {}"
          "".format(configuration.platform, configuration.method, configuration.communication))

    if configuration.method == "individual":
        if configuration.communication == 'write':

            simulation_methods.individual.write(configuration)
        elif configuration.communication == 'read':
            simulation_methods.individual.read(configuration)
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